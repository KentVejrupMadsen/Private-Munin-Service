#!/bin/bash

#
cat /proc/cpuinfo
cat /proc/stat

#
cat /proc/vmstat

#
cat /proc/interrupts
cat /proc/softirqs

#
cat /proc/loadavg

# Memory
cat /proc/meminfo

free -t

# Disks stats
cat /proc/diskstats
