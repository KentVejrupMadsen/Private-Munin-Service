#!/bin/bash

# Cpu, Divide by 1000
echo -n 'CPU|Temperature = '
cat /sys/class/thermal/thermal_zone0/temp

# Cpu, frequency, multiply by thousand to get hertz
echo -n 'CPU|Frequency = '
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq

# Gpu Temperature
echo -n 'GPU|Temperature = '
/opt/vc/bin/vcgencmd measure_temp