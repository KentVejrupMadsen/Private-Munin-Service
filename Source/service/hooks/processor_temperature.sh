#!/bin/bash

# retrieve sensor data and insert it into a file
cat /sys/class/thermal/thermal_zone0/temp > /tmp/munin-processor-temp-value

# get digit value
awk '{ sum = $1 / 1000 ; print sum }' /tmp/munin-processor-temp-value

# cleanup
rm /tmp/munin-processor-temp-value
