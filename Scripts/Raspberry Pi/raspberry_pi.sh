#!/bin/bash

echo '[memory] '
echo -n ' [arm] '
vcgencmd get_mem arm

echo -n ' [gpu] '
vcgencmd get_mem gpu

echo '[clock] '

echo -n ' [arm] '
vcgencmd measure_clock arm

echo -n ' [core] '
vcgencmd measure_clock core

echo -n ' [h264] '
vcgencmd measure_clock h264

echo -n ' [ips] '
vcgencmd measure_clock ips

echo -n ' [v3d] '
vcgencmd measure_clock v3d

echo -n ' [uart] '
vcgencmd measure_clock uart

echo -n ' [pwm] '
vcgencmd measure_clock pwm

echo -n ' [emmc] '
vcgencmd measure_clock emmc

echo -n ' [pixel] '
vcgencmd measure_clock pixel

echo -n ' [vec] '
vcgencmd measure_clock vec

echo -n ' [hdmi] '
vcgencmd measure_clock hdmi

echo -n ' [dpi] '
vcgencmd measure_clock dpi
