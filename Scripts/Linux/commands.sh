#!/bin/bash

echo "{ uptime }"
uptime
echo "{ end }"
echo ""

echo "{ free }"
free -t
echo "{ end }"
echo ""

echo "{ vmstat }"
vmstat
echo "{ end }"
echo ""

echo "{ netstat }"
netstat
echo "{ end }"
echo ""

echo "{ ps }"
ps
echo "{ end }"
echo ""

echo "{ ss }"
ss
echo "{ end }"
echo ""

echo "{ df }"
df
echo "{ end }"
echo ""

echo "{ nproc }"
nproc
echo "{ end }"
echo ""

echo "{ lscpu }"
lscpu
echo "{ end }"
echo ""

echo "{ lsblk }"
lsblk
echo "{ end }"
echo ""

echo "{ lsusb }"
lsusb
echo "{ end }"
echo ""

echo "{ lsof }"
lsof
echo "{ end }"
echo ""

echo "{ dmesg }"
dmesg
echo "{ end } "
echo ""