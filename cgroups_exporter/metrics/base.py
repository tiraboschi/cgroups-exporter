from functools import lru_cache
from pathlib import Path
from typing import NamedTuple

from ._metrics import INF, Metric

import os
import re


class CGroupTask(NamedTuple):
    abspath: Path
    base: Path
    group: str
    path: Path


class MetricProviderBase:
    def __init__(self, task: CGroupTask):
        self.task = task
        self.base_path = str(task.base)
        self.path = str(task.path)

    def __call__(self):
        raise NotImplementedError


class IntProviderBase(MetricProviderBase):
    FILENAME: str
    NAME: str
    METRIC: str
    DOCUMENTATION: str
    MAX_VALUE: str = "max"

    def check_inf(self, value):
        if value == self.MAX_VALUE:
            return INF

        return int(value)

    def __call__(self):
        fpath = self.task.abspath / self.FILENAME

        if not fpath.exists():
            return

        with open(fpath, "r") as fp:
            value = self.check_inf(fp.read().strip())

        metric = gauge_factory(
            self.NAME,
            self.METRIC,
            self.task.group.replace(",", "_"),
            self.DOCUMENTATION,
            labelnames=("base_path", "path"),
        )
        metric.labels(base_path=self.base_path, path=self.path).set(value)


@lru_cache(2 ** 20)
def gauge_factory(
    name: str,
    unit: str,
    group,
    documentation: str,
    labelnames=(),
    namespace: str = "cgroups",
) -> Metric:
    return Metric(
        name=name,
        help=documentation,
        labelnames=labelnames,
        namespace=namespace,
        subsystem=group,
        unit=unit,
    )


@lru_cache(2 ** 20)
def counter_factory(
    name: str,
    unit: str,
    group,
    documentation: str,
    labelnames=(),
    namespace: str = "cgroups",
) -> Metric:
    return Metric(
        type="counter",
        name=name,
        help=documentation,
        labelnames=labelnames,
        namespace=namespace,
        subsystem=group,
        unit=unit,
    )


class UsageBase(IntProviderBase):
    NAME = "usage"


class LimitBase(IntProviderBase):
    NAME = "limit"


class StatBase(MetricProviderBase):
    STAT_FILE: str
    DOCUMENTATION: str

    def __call__(self):
        stat = self.task.abspath / self.STAT_FILE
        if not stat.exists():
            return

        with open(stat, "r") as fp:
            for line in fp:
                param, value = line.strip().split(" ", 1)
                metric = gauge_factory(
                    "stat",
                    param,
                    self.task.group.replace(",", "_"),
                    self.DOCUMENTATION + " ({!r} field from {!r} file)".format(
                        param, self.STAT_FILE,
                    ),
                    labelnames=("base_path", "path"),
                )

                metric.labels(base_path=self.base_path, path=self.path).set(
                    int(value),
                )


class PressureBase(MetricProviderBase):
    PRESSURE_FILE: str
    DOCUMENTATION: str

    def __call__(self):
        stat = self.task.abspath / self.PRESSURE_FILE
        if not stat.exists():
            return

        with open(stat, "r") as fp:
            for line in fp:
                kind, metric = line.split(" ", 1)
                metrics = {}

                for part in metric.split(" "):
                    key, value = part.split("=")
                    metrics[key] = float(value) if "." in value else int(value)

                for key, value in metrics.items():
                    doc_suffix = ""
                    if "avg" in key:
                        doc_suffix = ". Average by {} seconds".format(
                            key.split("avg", 1)[-1],
                        )
                    if "total" in key:
                        doc_suffix = " total"

                    metric = gauge_factory(
                        kind,
                        key,
                        self.PRESSURE_FILE.replace(".", "_"),
                        self.DOCUMENTATION + doc_suffix,
                        labelnames=("base_path", "path"),
                    )

                    metric.labels(
                        base_path=self.base_path,
                        path=self.path,
                    ).set(
                        value,
                    )


SPLIT_PATH = re.compile(
    r"^kubepods-(?P<pod_class1>.*)\.slice/kubepods-(?P<pod_class2>.*)-pod(?P<pod_uid>.*)\.slice/?$"
)


class PodPSIBase(MetricProviderBase):
    PRESSURE_FILE: str
    DOCUMENTATION: str

    node_name = os.getenv("NODE_NAME") if os.getenv("NODE_NAME") is not None else "undetectable"

    def __call__(self):
        match = SPLIT_PATH.match(self.path)

        if match is None:
            return

        data = match.groupdict()
        pod_class1 = data.get("pod_class1")
        pod_class2 = data.get("pod_class2")
        pod_uid = data.get("pod_uid").replace("_", "-")
        if pod_class1 != pod_class2:
            return
        if not pod_uid:
            return

        stat = self.task.abspath / self.PRESSURE_FILE
        if not stat.exists():
            return

        with open(stat, "r") as fp:
            for line in fp:
                kind, metric = line.split(" ", 1)
                metrics = {}

                for part in metric.split(" "):
                    key, value = part.split("=")
                    metrics[key] = float(value) / 1e6

                for key, value in metrics.items():
                    doc_suffix = ""
                    altered_key = "seconds"
                    if "avg" in key:
                        continue
                    if "total" in key:
                        doc_suffix = " seconds total"

                    metric = counter_factory(
                        kind,
                        altered_key,
                        self.PRESSURE_FILE.replace(".", "_"),
                        self.DOCUMENTATION + doc_suffix,
                        labelnames=("pod_class", "pod_uid", "node_name"),
                        namespace="cgroupsv2kubepods",
                        )

                    metric.labels(
                        pod_class=pod_class1,
                        pod_uid=pod_uid,
                        node_name=self.node_name,
                    ).set(
                        value,
                    )


class PodStatBase(MetricProviderBase):
    STAT_FILE: str
    DOCUMENTATION: str

    node_name = os.getenv("NODE_NAME") if os.getenv("NODE_NAME") is not None else "undetectable"

    def __call__(self):
        match = SPLIT_PATH.match(self.path)

        if match is None:
            return

        data = match.groupdict()
        pod_class1 = data.get("pod_class1")
        pod_class2 = data.get("pod_class2")
        pod_uid = data.get("pod_uid").replace("_", "-")
        if pod_class1 != pod_class2:
            return
        if not pod_uid:
            return

        stat = self.task.abspath / self.STAT_FILE
        if not stat.exists():
            return

        with open(stat, "r") as fp:
            for line in fp:
                param, value = line.strip().split(" ", 1)
                metric = gauge_factory(
                    "stat",
                    param,
                    self.STAT_FILE.split(".")[0],
                    self.DOCUMENTATION + " ({!r} field from {!r} file)".format(
                        param, self.STAT_FILE,
                    ),
                    labelnames=("pod_class", "pod_uid", "node_name"),
                    namespace="cgroupsv2kubepods",
                    )

                metric.labels(
                    pod_class=pod_class1,
                    pod_uid=pod_uid,
                    node_name=self.node_name,
                ).set(
                    int(value),
                )
