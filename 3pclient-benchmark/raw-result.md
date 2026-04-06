### cli-freethreading

```
[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf record -F 99 --call-graph dwarf -g /home/ec2-user/aws-crt-s3-benchmarks/py-freethread/python/venv/bin/python3 /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-python/main.py cli-crt /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-1MiB-10_000x.run.json aws-c-s3-test-bucket-269381 us-west-2 200.0
start: 1775492892637632815
Run:1 Secs:16.192687 Gb/s:5.180492
[ perf record: Woken up 961 times to write data ]
[ perf record: Captured and wrote 250.261 MB perf.data (30311 samples) ]
```

### Java

#### Java client CRT

```
[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf script | /home/ec2-user/FlameGraph/stackcollapse-perf.pl | /home/ec2-user/FlameGraph/flamegraph.pl > cli-freethread.svg
[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf record -F 99 --call-graph dwarf -g java -jar /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-java/target/s3-benchrunner-java-1.0-SNAPSHOT.jar   sdk-java-client-crt   /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-1MiB-10_000x.run.json aws-c-s3-test-bucket-269381 us-west-2 200.0
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Run:1 Secs:3.666959 Gb/s:22.876196
Overall stats; Throughput Mean:22876.2 Mb/s Throughput Variance:Infinity Mb/s Duration Mean:3.667 s Duration Variance:0.000 s
```

#### Java transfer manager CRT

```
[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf record -F 99 --call-graph dwarf -g java -jar /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-java/target/s3-benchrunner-java-1.0-SNAPSHOT.jar   sdk-java-tm-crt   /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-1MiB-10_000x.run.json aws-c-s3-test-bucket-269381 us-west-2 200.0
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Run:1 Secs:9.889166 Gb/s:8.482624
Overall stats; Throughput Mean:8482.6 Mb/s Throughput Variance:Infinity Mb/s Duration Mean:9.889 s Duration Variance:0.000 s
```

#### Java transfer manager CRT with transferDirectoryMaxConcurrency 250

```
[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf record -F 99 --call-graph dwarf -g java -jar /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-java/target/s3-benchrunner-java-1.0-SNAPSHOT.jar   sdk-java-tm-crt   /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-1MiB-10_000x.run.json aws-c-s3-test-bucket-269381 us-west-2 200.0
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Run:1 Secs:7.342425 Gb/s:11.424847
Overall stats; Throughput Mean:11424.8 Mb/s Throughput Variance:Infinity Mb/s Duration Mean:7.342 s Duration Variance:0.000 s
[ perf record: Woken up 1034 times to write data ]
[ perf record: Captured and wrote 269.759 MB perf.data (33302 samples) ]
```

### s5cmd

```
[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf record -F 99 --call-graph dwarf -g /home/ec2-user/aws-crt-s3-benchmarks/py-freethread/python/venv/bin/python3 /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-3p/main.py /home/ec2-user/aws-crt-s3-benchmarks/build/s5cmd/bin/s5cmd s5cmd /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-1MiB-10_000x.run.json aws-c-s3-test-bucket-269381 us-west-2 200.0
Run:1 Secs:5.707553 Gb/s:14.697380
[ perf record: Woken up 1027 times to write data ]
[ perf record: Captured and wrote 272.846 MB perf.data (33786 samples) ]
```

### rclone

[ec2-user@ip-172-31-10-121 latest-3rd]$ sudo perf record -F 99 --call-graph dwarf -g /home/ec2-user/aws-crt-s3-benchmarks/py-freethread/python/venv/bin/python3 /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-3p/main.py /usr/bin/rclone rclone /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-1MiB-10_000x.run.json aws-c-s3-test-bucket-269381 us-west-2 200.0
Run:1 Secs:6.388493 Gb/s:13.130809
[ perf record: Woken up 441 times to write data ]
[ perf record: Captured and wrote 121.326 MB perf.data (15008 samples) ]
