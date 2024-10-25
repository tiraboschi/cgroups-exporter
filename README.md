# CGroups exporter

Exporter for CGroupsv2 (PSI and stats) metrics for k8s pods (`/sys/fs/cgroup/kubepods.slice/`).
This is a simple POC derived from: https://github.com/mosquito/cgroups-exporter

Collects metrics (PSI and stats) for all cgroupsv2 based pods, without the need to install separate exporters 
inside each container.

## Installation

It can be deployed on OCP with the manifests under `deploy_ocp`.
`cgroup_exporter_ds.yaml` will create a `DaemonSet` executing a  `cgroup-exporter` pod on each node.
It will also create a `Service` and a `ServiceMonitor` object to let `Prometheus` scrape it.
`Prometheus node exporter` is already collecting PSI metrics at node level. 

PSI is not enabled by default on RHCOS nodes but it can be easily enabled with a `MachineConfig` setting a `KernelParameter`. 

## Metrics

### PSI metrics

> [!IMPORTANT]
> PSI is not enabled by default on RHCOS nodes but it can be easily enabled with a `MachineConfig` setting a `KernelParameter`.

| Name                                        | Type    | Description                    |
|---------------------------------------------|---------|--------------------------------|
| `cgroupsv2kubepods_cpu_pressure_some_seconds`    | Counter | CPU resource pressure total    |
| `cgroupsv2kubepods_cpu_pressure_full_seconds`    | Counter | CPU resource pressure total    |
| `cgroupsv2kubepods_io_pressure_full_seconds`     | Counter | IO resource pressure total     |
| `cgroupsv2kubepods_io_pressure_full_seconds`     | Counter | IO resource pressure total     |
| `cgroupsv2kubepods_memory_pressure_full_seconds` | Counter | Memory resource pressure total |
| `cgroupsv2kubepods_memory_pressure_full_seconds` | Counter | Memory resource pressure total |

[Prometheus Node exporter](https://github.com/prometheus/node_exporter?tab=readme-ov-file#enabled-by-default) is already collecting by default (if enabled at Kernel level) PSI metrics at node level.
No need to replicate it here.

| Name                                         | Type    | Description                                                                    |
|----------------------------------------------|---------|--------------------------------------------------------------------------------|
| `node_pressure_cpu_waiting_seconds_total`    | Counter | Total time in seconds that processes have waited for CPU time                  |
| `node_pressure_memory_stalled_seconds_total` | Counter | Total time in seconds no process could make progress due to memory congestion  |
| `node_pressure_memory_waiting_seconds_total` | Counter | Total time in seconds that processes have waited for memory                    |
| `node_pressure_io_stalled_seconds_total`     | Counter | Total time in seconds no process could make progress due to IO congestion      |
| `node_pressure_io_waiting_seconds_total`     | Counter | Total time in seconds that processes have waited due to IO congestion          |


### CPU stat metrics

| Name                                                    | Type  | Description                                             |
|---------------------------------------------------------|-------|---------------------------------------------------------|
| `cgroupsv2kubepods_cpu_stat_usage_usec`                 | Gauge | `usage_usec` field from `cpu.stat` file                 |
| `cgroupsv2kubepods_cpu_stat_user_usec`                  | Gauge | `user_usec` field from `cpu.stat` file                  |
| `cgroupsv2kubepods_cpu_stat_system_usec`                | Gauge | `system_usec` field from `cpu.stat` file                |
| `cgroupsv2kubepods_cpu_stat_core_sched_force_idle_usec` | Gauge | `core_sched.force_idle_usec` field from `cpu.stat` file |
| `cgroupsv2kubepods_cpu_stat_nr_periods`                 | Gauge | `nr_periods` field from `cpu.stat` file                 |
| `cgroupsv2kubepods_cpu_stat_nr_throttled`               | Gauge | `nr_throttled` field from `cpu.stat` file               |
| `cgroupsv2kubepods_cpu_stat_throttled_usec`             | Gauge | `throttled_usec` field from `cpu.stat` file             |
| `cgroupsv2kubepods_cpu_stat_nr_bursts`                  | Gauge | `nr_bursts` field from `cpu.stat` file                  |
| `cgroupsv2kubepods_cpu_stat_burst_usec`                 | Gauge | `burst_usec` field from `cpu.stat` file                 |


### Memory stat metrics

| Name                                                     | Type  | Description                                              |
|----------------------------------------------------------|-------|----------------------------------------------------------|
| `cgroupsv2kubepods_memory_stat_anon`                     | Gauge | `anon` field from `memory.stat` file                     |
| `cgroupsv2kubepods_memory_stat_file`                     | Gauge | `file` field from `memory.stat` file                     |
| `cgroupsv2kubepods_memory_stat_kernel`                   | Gauge | `kernel` field from `memory.stat` file                   |
| `cgroupsv2kubepods_memory_stat_kernel_stack`             | Gauge | `kernel_stack` field from `memory.stat` file             |
| `cgroupsv2kubepods_memory_stat_pagetables`               | Gauge | `pagetables` field from `memory.stat` file               |
| `cgroupsv2kubepods_memory_stat_sec_pagetables`           | Gauge | `sec_pagetables` field from `memory.stat` file           |
| `cgroupsv2kubepods_memory_stat_percpu`                   | Gauge | `percpu` field from `memory.stat` file                   |
| `cgroupsv2kubepods_memory_stat_sock`                     | Gauge | `sock` field from `memory.stat` file                     |
| `cgroupsv2kubepods_memory_stat_vmalloc`                  | Gauge | `vmalloc` field from `memory.stat` file                  |
| `cgroupsv2kubepods_memory_stat_shmem`                    | Gauge | `shmem` field from `memory.stat` file                    |
| `cgroupsv2kubepods_memory_stat_zswap`                    | Gauge | `zswap` field from `memory.stat` file                    |
| `cgroupsv2kubepods_memory_stat_zswapped`                 | Gauge | `zswapped` field from `memory.stat` file                 |
| `cgroupsv2kubepods_memory_stat_file_mapped`              | Gauge | `file_mapped` field from `memory.stat` file              |
| `cgroupsv2kubepods_memory_stat_file_dirty`               | Gauge | `file_dirty` field from `memory.stat` file               |
| `cgroupsv2kubepods_memory_stat_file_writeback`           | Gauge | `file_writeback` field from `memory.stat` file           |
| `cgroupsv2kubepods_memory_stat_swapcached`               | Gauge | `swapcached` field from `memory.stat` file               |
| `cgroupsv2kubepods_memory_stat_anon_thp`                 | Gauge | `anon_thp` field from `memory.stat` file                 |
| `cgroupsv2kubepods_memory_stat_file_thp`                 | Gauge | `file_thp` field from `memory.stat` file                 |
| `cgroupsv2kubepods_memory_stat_shmem_thp`                | Gauge | `shmem_thp` field from `memory.stat` file                |
| `cgroupsv2kubepods_memory_stat_inactive_anon`            | Gauge | `inactive_anon` field from `memory.stat` file            |
| `cgroupsv2kubepods_memory_stat_active_anon`              | Gauge | `active_anon` field from `memory.stat` file              |
| `cgroupsv2kubepods_memory_stat_inactive_file`            | Gauge | `inactive_file` field from `memory.stat` file            |
| `cgroupsv2kubepods_memory_stat_active_file`              | Gauge | `active_file` field from `memory.stat` file              |
| `cgroupsv2kubepods_memory_stat_unevictable`              | Gauge | `unevictable` field from `memory.stat` file              |
| `cgroupsv2kubepods_memory_stat_slab_reclaimable`         | Gauge | `slab_reclaimable` field from `memory.stat` file         |
| `cgroupsv2kubepods_memory_stat_slab_unreclaimable`       | Gauge | `slab_unreclaimable` field from `memory.stat` file       |
| `cgroupsv2kubepods_memory_stat_slab`                     | Gauge | `slab` field from `memory.stat` file                     |
| `cgroupsv2kubepods_memory_stat_workingset_refault_anon`  | Gauge | `workingset_refault_anon` field from `memory.stat` file  |
| `cgroupsv2kubepods_memory_stat_workingset_refault_file`  | Gauge | `workingset_refault_file` field from `memory.stat` file  |
| `cgroupsv2kubepods_memory_stat_workingset_activate_anon` | Gauge | `workingset_activate_anon` field from `memory.stat` file |
| `cgroupsv2kubepods_memory_stat_workingset_activate_file` | Gauge | `workingset_activate_file` field from `memory.stat` file |
| `cgroupsv2kubepods_memory_stat_workingset_restore_anon`  | Gauge | `workingset_restore_anon` field from `memory.stat` file  |
| `cgroupsv2kubepods_memory_stat_workingset_restore_file`  | Gauge | `workingset_restore_file` field from `memory.stat` file  |
| `cgroupsv2kubepods_memory_stat_workingset_nodereclaim`   | Gauge | `workingset_nodereclaim` field from `memory.stat` file   |
| `cgroupsv2kubepods_memory_stat_pgscan`                   | Gauge | `pgscan` field from `memory.stat` file                   |
| `cgroupsv2kubepods_memory_stat_pgsteal`                  | Gauge | `pgsteal` field from `memory.stat` file                  |
| `cgroupsv2kubepods_memory_stat_pgscan_kswapd`            | Gauge | `pgscan_kswapd` field from `memory.stat` file            |
| `cgroupsv2kubepods_memory_stat_pgscan_direct`            | Gauge | `pgscan_direct` field from `memory.stat` file            |
| `cgroupsv2kubepods_memory_stat_pgscan_khugepaged`        | Gauge | `pgscan_khugepaged` field from `memory.stat` file        |
| `cgroupsv2kubepods_memory_stat_pgsteal_kswapd`           | Gauge | `pgsteal_kswapd` field from `memory.stat` file           |
| `cgroupsv2kubepods_memory_stat_pgsteal_direct`           | Gauge | `pgsteal_direct` field from `memory.stat` file           |
| `cgroupsv2kubepods_memory_stat_pgsteal_khugepaged`       | Gauge | `pgsteal_khugepaged` field from `memory.stat` file       |
| `cgroupsv2kubepods_memory_stat_pgfault`                  | Gauge | `pgfault` field from `memory.stat` file                  |
| `cgroupsv2kubepods_memory_stat_pgmajfault`               | Gauge | `pgmajfault` field from `memory.stat` file               |
| `cgroupsv2kubepods_memory_stat_pgrefill`                 | Gauge | `pgrefill` field from `memory.stat` file                 |
| `cgroupsv2kubepods_memory_stat_pgactivate`               | Gauge | `pgactivate` field from `memory.stat` file               |
| `cgroupsv2kubepods_memory_stat_pgdeactivate`             | Gauge | `pgdeactivate` field from `memory.stat` file             |
| `cgroupsv2kubepods_memory_stat_pglazyfree`               | Gauge | `pglazyfree` field from `memory.stat` file               |
| `cgroupsv2kubepods_memory_stat_pglazyfreed`              | Gauge | `pglazyfreed` field from `memory.stat` file              |
| `cgroupsv2kubepods_memory_stat_zswpin`                   | Gauge | `zswpin` field from `memory.stat` file                   |
| `cgroupsv2kubepods_memory_stat_zswpout`                  | Gauge | `zswpout` field from `memory.stat` file                  |
| `cgroupsv2kubepods_memory_stat_thp_fault_alloc`          | Gauge | `thp_fault_alloc` field from `memory.stat` file          |
| `cgroupsv2kubepods_memory_stat_thp_collapse_alloc`       | Gauge | `thp_collapse_alloc` field from `memory.stat` file       |
