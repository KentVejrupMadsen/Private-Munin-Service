#!/bin/bash

# Cpu, Divide by 1000
echo '[CPU] [Temperature] '
cat /sys/class/thermal/thermal_zone0/temp

# Cpu, frequency, multiply by thousand to get hertz
echo '[CPU] [Frequency]'
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq

cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq

# Gpu Temperature
echo '[GPU] [Temperature] '
/opt/vc/bin/vcgencmd measure_temp