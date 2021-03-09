#!/bin/sh

for f in /bigdata/data/airline-on-time-performance/inflated/On_Time_On_Time_Performance_*.csv;
do cat $f | csvcut -d "," -f 35 | tail -n +2; done | awk '{sum += $0}; {mean = sum/NR}; END {print(mean)}'