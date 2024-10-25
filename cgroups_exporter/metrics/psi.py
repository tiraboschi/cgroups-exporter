import logging

from .base import CGroupTask, PodPSIBase


log = logging.getLogger()


def psi_collector(task: CGroupTask):
    for collector in COLLECTORS:
        try:
            collector(task)()
        except Exception:
            log.exception("Failed to collect %r", collector)


class PSICPUPressure(PodPSIBase):
    PRESSURE_FILE = "cpu.pressure"
    DOCUMENTATION = "CPU resource pressure"


class PSIIOPressure(PodPSIBase):
    PRESSURE_FILE = "io.pressure"
    DOCUMENTATION = "IO resource pressure"


class PSIMemoryPressure(PodPSIBase):
    PRESSURE_FILE = "memory.pressure"
    DOCUMENTATION = "Memory resource pressure"


COLLECTORS = (
    PSICPUPressure,
    PSIIOPressure,
    PSIMemoryPressure,
)
