## C

```
(venv) [ec2-user@ip-172-31-10-121 c-perf]$ sudo perf record -F 99 --call-graph dwarf  -g  /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-c/build/s3-benchrunner-c crt-c ~/aws-crt-s3-benchmarks/workloads/download-5GiB-1x.run.json  aws-c-s3-test-bucket-269381--usw2-az1--x-s3 us-west-2 200.0
Run:1 Secs:3.049503 Gb/s:14.084155
Overall Throughput (Gb/s) Median:14.084155 Mean:14.084155 Min:14.084155 Max:14.084155 Variance:0.000000 StdDev:0.000000
Overall Duration (Secs) Median:3.049503 Mean:3.049503 Min:3.049503 Max:3.049503 Variance:0.000000 StdDev:0.000000
Peak RSS:5178.589844 MiB
[ perf record: Woken up 52 times to write data ]
[ perf record: Captured and wrote 21.333 MB perf.data (2522 samples) ]
```

## Python

```
(venv) [ec2-user@ip-172-31-10-121 more-python]$ sudo perf record -F 99 --call-graph dwarf  -g ~/aws-crt-s3-benchmarks/build/python/venv/bin/python /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-python/main.py crt-python   /home/ec2-user/aws-crt-s3-benchmarks/workloads/download-5GiB-1x.run.json   aws-c-s3-test-bucket-269381--usw2-az1--x-s3 us-west-2 200.0
Run:1 Secs:3.291192 Gb/s:13.049885
[ perf record: Woken up 57 times to write data ]
[ perf record: Captured and wrote 20.493 MB perf.data (2423 samples) ]
```

## Java

```
(venv) [ec2-user@ip-172-31-10-121 java-perf]$ sudo perf record -F 99 --call-graph dwarf  -g java -jar /home/ec2-user/aws-crt-s3-benchmarks/runners/s3-benchrunner-java/target/s3-benchrunner-java-1.0-SNAPSHOT.jar crt-java   ~/aws-crt-s3-benchmarks/workloads/download-5GiB-1x.run.json   aws-c-s3-test-bucket-269381--usw2-az1--x-s3 us-west-2 200.0
Run:1 Secs:3.047009 Gb/s:14.095684
Overall stats; Throughput Mean:14095.7 Mb/s Throughput Variance:Infinity Mb/s Duration Mean:3.047 s Duration Variance:0.000 s
[ perf record: Woken up 78 times to write data ]
[ perf record: Captured and wrote 27.163 MB perf.data (3243 samples) ]
```
