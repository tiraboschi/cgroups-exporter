CGroups exporter
================

Exporter for CGroups metrics, for LXD/Docker/systemd.

Installation
------------

```bash
pip install cgroups-exporter
cgroups-exporter --cgroups-path "/sys/fs/cgroup/*/lxc.payload.*"
```


Usage
-----

Args that start with `--` (eg. -s) can also be set in a config file 
(`~/.cgroups-exporter.conf` or `/etc/cgroups-exporter.conf`). 

Config file syntax allows: `key=value`, `flag=true`, `stuff=[a,b,c]` 
(for details, see syntax [here](https://goo.gl/R74nmi)). 

If an arg is specified in more than one place, then commandline values 
override environment variables which override config file values 
which override defaults.

```
usage: cgroups-exporter [-h]
                        [-s POOL_SIZE]
                        [-u USER]
                        [--log-level {debug,info,warning,error,fatal}]
                        [--log-format {stream,color,json,syslog}]
                        [--metrics-address METRICS_ADDRESS]
                        [--metrics-port METRICS_PORT]
                        --cgroups-path CGROUPS_PATH [CGROUPS_PATH ...]
                        [--collector-interval COLLECTOR_INTERVAL]
                        [--collector-delay COLLECTOR_DELAY]
                        [--collector-workers COLLECTOR_WORKERS]
                        [--profiler]
                        [--profiler-interval PROFILER_INTERVAL]
                        [--profiler-top-results PROFILER_TOP_RESULTS]
                        [--memory-tracer]
                        [--memory-tracer-interval MEMORY_TRACER_INTERVAL]
                        [--memory-tracer-top-results MEMORY_TRACER_TOP_RESULTS]

optional arguments:

  -h, --help            show this help message and exit
  -s POOL_SIZE, --pool-size POOL_SIZE
                        Thread pool size [env var: CGROUPS_EXPORTER_POOL_SIZE] (default: 4)
  -u USER, --user USER  Change process UID [env var: CGROUPS_EXPORTER_USER] (default: None)

Logging options:
  --log-level {debug,info,warning,error,fatal}
                        [env var: CGROUPS_EXPORTER_LOG_LEVEL] (default: info)
  --log-format {stream,color,json,syslog}
                        [env var: CGROUPS_EXPORTER_LOG_FORMAT] (default: color)

Metrics API options:
  --metrics-address METRICS_ADDRESS
                        [env var: CGROUPS_EXPORTER_METRICS_ADDRESS] (default: ::)
  --metrics-port METRICS_PORT
                        [env var: CGROUPS_EXPORTER_METRICS_PORT] (default: 9735)

Cgroups options:
  --cgroups-path CGROUPS_PATH [CGROUPS_PATH ...]
                        [env var: CGROUPS_EXPORTER_CGROUPS_PATH] (default: None)
  --collector-interval COLLECTOR_INTERVAL
                        [env var: CGROUPS_EXPORTER_COLLECTOR_INTERVAL] (default: 15.0)
  --collector-delay COLLECTOR_DELAY
                        [env var: CGROUPS_EXPORTER_COLLECTOR_DELAY] (default: 2.0)
  --collector-workers COLLECTOR_WORKERS
                        [env var: CGROUPS_EXPORTER_COLLECTOR_WORKERS] (default: 4)

Profiler settings:
  --profiler            [env var: CGROUPS_EXPORTER_PROFILER] (default: False)
  --profiler-interval PROFILER_INTERVAL
                        [env var: CGROUPS_EXPORTER_PROFILER_INTERVAL] (default: 5)
  --profiler-top-results PROFILER_TOP_RESULTS
                        [env var: CGROUPS_EXPORTER_PROFILER_TOP_RESULTS] (default: 20)

Memory tracer settings:
  --memory-tracer       [env var: CGROUPS_EXPORTER_MEMORY_TRACER] (default: False)
  --memory-tracer-interval MEMORY_TRACER_INTERVAL
                        [env var: CGROUPS_EXPORTER_MEMORY_TRACER_INTERVAL] (default: 5)
  --memory-tracer-top-results MEMORY_TRACER_TOP_RESULTS
                        [env var: CGROUPS_EXPORTER_MEMORY_TRACER_TOP_RESULTS] (default: 20)
```

Metrics
-------

| Name | Description |
| ------------ | ------------ |
| `cgroups_blkio_bfq_service_bytes_async` | BlockIO service bytes ('async' field from 'blkio.bfq.io_service_bytes' file) |
| `cgroups_blkio_bfq_service_bytes_discard` | BlockIO service bytes ('discard' field from 'blkio.bfq.io_service_bytes' file) |
| `cgroups_blkio_bfq_service_bytes_read` | BlockIO service bytes ('read' field from 'blkio.bfq.io_service_bytes' file) |
| `cgroups_blkio_bfq_service_bytes_recursive_async` | BlockIO service bytes recursive ('async' field from 'blkio.bfq.io_service_bytes_recursive' file) |
| `cgroups_blkio_bfq_service_bytes_recursive_discard` | BlockIO service bytes recursive ('discard' field from 'blkio.bfq.io_service_bytes_recursive' file) |
| `cgroups_blkio_bfq_service_bytes_recursive_read` | BlockIO service bytes recursive ('read' field from 'blkio.bfq.io_service_bytes_recursive' file) |
| `cgroups_blkio_bfq_service_bytes_recursive_sync` | BlockIO service bytes recursive ('sync' field from 'blkio.bfq.io_service_bytes_recursive' file) |
| `cgroups_blkio_bfq_service_bytes_recursive_total` | BlockIO service bytes recursive ('total' field from 'blkio.bfq.io_service_bytes_recursive' file) |
| `cgroups_blkio_bfq_service_bytes_recursive_write` | BlockIO service bytes recursive ('write' field from 'blkio.bfq.io_service_bytes_recursive' file) |
| `cgroups_blkio_bfq_service_bytes_sync` | BlockIO service bytes ('sync' field from 'blkio.bfq.io_service_bytes' file) |
| `cgroups_blkio_bfq_service_bytes_total` | BlockIO service bytes ('total' field from 'blkio.bfq.io_service_bytes' file) |
| `cgroups_blkio_bfq_service_bytes_write` | BlockIO service bytes ('write' field from 'blkio.bfq.io_service_bytes' file) |
| `cgroups_blkio_bfq_serviced_async` | BlockIO serviced bytes ('async' field from 'blkio.bfq.io_serviced' file) |
| `cgroups_blkio_bfq_serviced_discard` | BlockIO serviced bytes ('discard' field from 'blkio.bfq.io_serviced' file) |
| `cgroups_blkio_bfq_serviced_read` | BlockIO serviced bytes ('read' field from 'blkio.bfq.io_serviced' file) |
| `cgroups_blkio_bfq_serviced_recursive_async` | BlockIO serviced bytes recursive ('async' field from 'blkio.bfq.io_serviced_recursive' file) |
| `cgroups_blkio_bfq_serviced_recursive_discard` | BlockIO serviced bytes recursive ('discard' field from 'blkio.bfq.io_serviced_recursive' file) |
| `cgroups_blkio_bfq_serviced_recursive_read` | BlockIO serviced bytes recursive ('read' field from 'blkio.bfq.io_serviced_recursive' file) |
| `cgroups_blkio_bfq_serviced_recursive_sync` | BlockIO serviced bytes recursive ('sync' field from 'blkio.bfq.io_serviced_recursive' file) |
| `cgroups_blkio_bfq_serviced_recursive_total` | BlockIO serviced bytes recursive ('total' field from 'blkio.bfq.io_serviced_recursive' file) |
| `cgroups_blkio_bfq_serviced_recursive_write` | BlockIO serviced bytes recursive ('write' field from 'blkio.bfq.io_serviced_recursive' file) |
| `cgroups_blkio_bfq_serviced_sync` | BlockIO serviced bytes ('sync' field from 'blkio.bfq.io_serviced' file) |
| `cgroups_blkio_bfq_serviced_total` | BlockIO serviced bytes ('total' field from 'blkio.bfq.io_serviced' file) |
| `cgroups_blkio_bfq_serviced_write` | BlockIO serviced bytes ('write' field from 'blkio.bfq.io_serviced' file) |
| `cgroups_blkio_throttle_service_bytes_async` | BlockIO service bytes ('async' field from 'blkio.throttle.io_service_bytes' file) |
| `cgroups_blkio_throttle_service_bytes_discard` | BlockIO service bytes ('discard' field from 'blkio.throttle.io_service_bytes' file) |
| `cgroups_blkio_throttle_service_bytes_read` | BlockIO service bytes ('read' field from 'blkio.throttle.io_service_bytes' file) |
| `cgroups_blkio_throttle_service_bytes_recursive_async` | BlockIO throttle serviced bytes ('async' field from 'blkio.throttle.io_service_bytes_recursive' file) |
| `cgroups_blkio_throttle_service_bytes_recursive_discard` | BlockIO throttle serviced bytes ('discard' field from 'blkio.throttle.io_service_bytes_recursive' file) |
| `cgroups_blkio_throttle_service_bytes_recursive_read` | BlockIO throttle serviced bytes ('read' field from 'blkio.throttle.io_service_bytes_recursive' file) |
| `cgroups_blkio_throttle_service_bytes_recursive_sync` | BlockIO throttle serviced bytes ('sync' field from 'blkio.throttle.io_service_bytes_recursive' file) |
| `cgroups_blkio_throttle_service_bytes_recursive_total` | BlockIO throttle serviced bytes ('total' field from 'blkio.throttle.io_service_bytes_recursive' file) |
| `cgroups_blkio_throttle_service_bytes_recursive_write` | BlockIO throttle serviced bytes ('write' field from 'blkio.throttle.io_service_bytes_recursive' file) |
| `cgroups_blkio_throttle_service_bytes_sync` | BlockIO service bytes ('sync' field from 'blkio.throttle.io_service_bytes' file) |
| `cgroups_blkio_throttle_service_bytes_total` | BlockIO service bytes ('total' field from 'blkio.throttle.io_service_bytes' file) |
| `cgroups_blkio_throttle_service_bytes_write` | BlockIO service bytes ('write' field from 'blkio.throttle.io_service_bytes' file) |
| `cgroups_blkio_throttle_serviced_async` | BlockIO serviced bytes ('async' field from 'blkio.throttle.io_serviced' file) |
| `cgroups_blkio_throttle_serviced_discard` | BlockIO serviced bytes ('discard' field from 'blkio.throttle.io_serviced' file) |
| `cgroups_blkio_throttle_serviced_read` | BlockIO serviced bytes ('read' field from 'blkio.throttle.io_serviced' file) |
| `cgroups_blkio_throttle_serviced_recursive_async` | BlockIO serviced bytes recursive ('async' field from 'blkio.throttle.io_serviced_recursive' file) |
| `cgroups_blkio_throttle_serviced_recursive_discard` | BlockIO serviced bytes recursive ('discard' field from 'blkio.throttle.io_serviced_recursive' file) |
| `cgroups_blkio_throttle_serviced_recursive_read` | BlockIO serviced bytes recursive ('read' field from 'blkio.throttle.io_serviced_recursive' file) |
| `cgroups_blkio_throttle_serviced_recursive_sync` | BlockIO serviced bytes recursive ('sync' field from 'blkio.throttle.io_serviced_recursive' file) |
| `cgroups_blkio_throttle_serviced_recursive_total` | BlockIO serviced bytes recursive ('total' field from 'blkio.throttle.io_serviced_recursive' file) |
| `cgroups_blkio_throttle_serviced_recursive_write` | BlockIO serviced bytes recursive ('write' field from 'blkio.throttle.io_serviced_recursive' file) |
| `cgroups_blkio_throttle_serviced_sync` | BlockIO serviced bytes ('sync' field from 'blkio.throttle.io_serviced' file) |
| `cgroups_blkio_throttle_serviced_total` | BlockIO serviced bytes ('total' field from 'blkio.throttle.io_serviced' file) |
| `cgroups_blkio_throttle_serviced_write` | BlockIO serviced bytes ('write' field from 'blkio.throttle.io_serviced' file) |
| `cgroups_cpu_cpuacct_cfs_period_us` | Allowed CPU periods in microseconds |
| `cgroups_cpu_cpuacct_cfs_quota_us` | Allowed CPU quota in microseconds |
| `cgroups_cpu_cpuacct_shares` | Allowed CPU shares |
| `cgroups_cpu_cpuacct_stat_nr_periods` | CPU statistic ('nr_periods' field from 'cpu.stat' file) |
| `cgroups_cpu_cpuacct_stat_nr_throttled` | CPU statistic ('nr_throttled' field from 'cpu.stat' file) |
| `cgroups_cpu_cpuacct_stat_system` | CPU accounting statistic ('system' field from 'cpuacct.stat' file) |
| `cgroups_cpu_cpuacct_stat_throttled_time` | CPU statistic ('throttled_time' field from 'cpu.stat' file) |
| `cgroups_cpu_cpuacct_stat_user` | CPU accounting statistic ('user' field from 'cpuacct.stat' file) |
| `cgroups_cpu_pressure_some_avg10` | CPU resource pressure. Average by 10 seconds |
| `cgroups_cpu_pressure_some_avg300` | CPU resource pressure. Average by 300 seconds |
| `cgroups_cpu_pressure_some_avg60` | CPU resource pressure. Average by 60 seconds |
| `cgroups_cpu_pressure_some_total` | CPU resource pressure total |
| `cgroups_cpuset_count_cpu` | CPU set for the cgroup |
| `cgroups_exporter_calls_collector_created` | Exporter collector run counter |
| `cgroups_exporter_calls_collector_total` | Exporter collector run counter |
| `cgroups_exporter_collect_time_collector_created` | Exporter collector execution time |
| `cgroups_exporter_collect_time_collector` | Exporter collector execution time |
| `cgroups_io_pressure_full_avg10` | IO resource pressure. Average by 10 seconds |
| `cgroups_io_pressure_full_avg300` | IO resource pressure. Average by 300 seconds |
| `cgroups_io_pressure_full_avg60` | IO resource pressure. Average by 60 seconds |
| `cgroups_io_pressure_full_total` | IO resource pressure total |
| `cgroups_io_pressure_some_avg10` | IO resource pressure. Average by 10 seconds |
| `cgroups_io_pressure_some_avg300` | IO resource pressure. Average by 300 seconds |
| `cgroups_io_pressure_some_avg60` | IO resource pressure. Average by 60 seconds |
| `cgroups_io_pressure_some_total` | IO resource pressure total |
| `cgroups_memory_limit_kmem_tcp` | Kernel TCP memory limit |
| `cgroups_memory_limit_kmem` | Memory kernel limit |
| `cgroups_memory_limit_soft` | Soft limit |
| `cgroups_memory_limit_swap` | Swap limit |
| `cgroups_memory_limit` | Memory limit |
| `cgroups_memory_pressure_full_avg10` | Memory resource pressure. Average by 10 seconds |
| `cgroups_memory_pressure_full_avg300` | Memory resource pressure. Average by 300 seconds |
| `cgroups_memory_pressure_full_avg60` | Memory resource pressure. Average by 60 seconds |
| `cgroups_memory_pressure_full_total` | Memory resource pressure total |
| `cgroups_memory_pressure_some_avg10` | Memory resource pressure. Average by 10 seconds |
| `cgroups_memory_pressure_some_avg300` | Memory resource pressure. Average by 300 seconds |
| `cgroups_memory_pressure_some_avg60` | Memory resource pressure. Average by 60 seconds |
| `cgroups_memory_pressure_some_total` | Memory resource pressure total |
| `cgroups_memory_stat_active_anon` | memory statistic ('active_anon' field from 'memory.stat' file) |
| `cgroups_memory_stat_active_file` | memory statistic ('active_file' field from 'memory.stat' file) |
| `cgroups_memory_stat_cache` | memory statistic ('cache' field from 'memory.stat' file) |
| `cgroups_memory_stat_dirty` | memory statistic ('dirty' field from 'memory.stat' file) |
| `cgroups_memory_stat_hierarchical_memory_limit` | memory statistic ('hierarchical_memory_limit' field from 'memory.stat' file) |
| `cgroups_memory_stat_hierarchical_memsw_limit` | memory statistic ('hierarchical_memsw_limit' field from 'memory.stat' file) |
| `cgroups_memory_stat_inactive_anon` | memory statistic ('inactive_anon' field from 'memory.stat' file) |
| `cgroups_memory_stat_inactive_file` | memory statistic ('inactive_file' field from 'memory.stat' file) |
| `cgroups_memory_stat_mapped_file` | memory statistic ('mapped_file' field from 'memory.stat' file) |
| `cgroups_memory_stat_pgfault` | memory statistic ('pgfault' field from 'memory.stat' file) |
| `cgroups_memory_stat_pgmajfault` | memory statistic ('pgmajfault' field from 'memory.stat' file) |
| `cgroups_memory_stat_pgpgin` | memory statistic ('pgpgin' field from 'memory.stat' file) |
| `cgroups_memory_stat_pgpgout` | memory statistic ('pgpgout' field from 'memory.stat' file) |
| `cgroups_memory_stat_rss_huge` | memory statistic ('rss_huge' field from 'memory.stat' file) |
| `cgroups_memory_stat_rss` | memory statistic ('rss' field from 'memory.stat' file) |
| `cgroups_memory_stat_shmem` | memory statistic ('shmem' field from 'memory.stat' file) |
| `cgroups_memory_stat_swap` | memory statistic ('swap' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_active_anon` | memory statistic ('total_active_anon' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_active_file` | memory statistic ('total_active_file' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_cache` | memory statistic ('total_cache' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_dirty` | memory statistic ('total_dirty' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_inactive_anon` | memory statistic ('total_inactive_anon' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_inactive_file` | memory statistic ('total_inactive_file' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_mapped_file` | memory statistic ('total_mapped_file' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_pgfault` | memory statistic ('total_pgfault' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_pgmajfault` | memory statistic ('total_pgmajfault' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_pgpgin` | memory statistic ('total_pgpgin' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_pgpgout` | memory statistic ('total_pgpgout' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_rss_huge` | memory statistic ('total_rss_huge' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_rss` | memory statistic ('total_rss' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_shmem` | memory statistic ('total_shmem' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_swap` | memory statistic ('total_swap' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_unevictable` | memory statistic ('total_unevictable' field from 'memory.stat' file) |
| `cgroups_memory_stat_total_writeback` | memory statistic ('total_writeback' field from 'memory.stat' file) |
| `cgroups_memory_stat_unevictable` | memory statistic ('unevictable' field from 'memory.stat' file) |
| `cgroups_memory_stat_writeback` | memory statistic ('writeback' field from 'memory.stat' file) |
| `cgroups_memory_usage_kmem_max` | Maximum kernel memory usage |
| `cgroups_memory_usage_kmem_tcp` | Kernel TCP memory usage |
| `cgroups_memory_usage_kmem` | Maximum kernel TCP maximum memory usage |
| `cgroups_memory_usage_max` | Maximum memory usage |
| `cgroups_memory_usage_swap_max` | Maximum swap usage |
| `cgroups_memory_usage_swap` | Swap usage |
| `cgroups_memory_usage` | Memory usage |
| `cgroups_pids_count` | Process IDs count for this namespace |
| `cgroups_unified_stat_system_usec` | CPU statistic ('system_usec' field from 'cpu.stat' file) |
| `cgroups_unified_stat_usage_usec` | CPU statistic ('usage_usec' field from 'cpu.stat' file) |
| `cgroups_unified_stat_user_usec` | CPU statistic ('user_usec' field from 'cpu.stat' file) |
