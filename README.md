CGroups exporter
================

Exporter for CGroupsv2 PSI metrics for k8s pods.
This is a simple POC derived from: https://github.com/mosquito/cgroups-exporter

Collects PSI metrics for all cgroupsv2 based pods, without the need to install separate exporters 
inside each container.

Installation
------------

It can be deployed on OCP with the manifests under `deploy_ocp`.
`cgroup_exporter_ds.yaml` will create a `DaemonSet` executing a  `cgroup-exporter` pod on each node.
It will also create a `Service` and a `ServiceMonitor` object to let `Prometheus` scrape it.
`Prometheus node exporter` is already collecting PSI metrics at node level. 

PSI is not enabled by default on RHCOS nodes but it can be easily enabled with a `MachineConfig` setting a `KernelParameter`. 

Metrics
-------

| Name                                        | Type    | Description                    |
|---------------------------------------------|---------|--------------------------------|
| `cgroupsv2psi_cpu_pressure_some_seconds`    | Counter | CPU resource pressure total    |
| `cgroupsv2psi_cpu_pressure_full_seconds`    | Counter | CPU resource pressure total    |
| `cgroupsv2psi_io_pressure_full_seconds`     | Counter | IO resource pressure total     |
| `cgroupsv2psi_io_pressure_full_seconds`     | Counter | IO resource pressure total     |
| `cgroupsv2psi_memory_pressure_full_seconds` | Counter | Memory resource pressure total |
| `cgroupsv2psi_memory_pressure_full_seconds` | Counter | Memory resource pressure total |

[Prometheus Node exporter](https://github.com/prometheus/node_exporter?tab=readme-ov-file#enabled-by-default) is already collecting by default (if enabled at Kernel level) PSI metrics at node level.
No need to replicate it here.

| Name                                         | Type    | Description                                                                    |
|----------------------------------------------|---------|--------------------------------------------------------------------------------|
| `node_pressure_cpu_waiting_seconds_total`    | Counter | Total time in seconds that processes have waited for CPU time                  |
| `node_pressure_memory_stalled_seconds_total` | Counter | Total time in seconds no process could make progress due to memory congestion  |
| `node_pressure_memory_waiting_seconds_total` | Counter | Total time in seconds that processes have waited for memory                    |
| `node_pressure_io_stalled_seconds_total`     | Counter | Total time in seconds no process could make progress due to IO congestion      |
| `node_pressure_io_waiting_seconds_total`     | Counter | Total time in seconds that processes have waited due to IO congestion          |
