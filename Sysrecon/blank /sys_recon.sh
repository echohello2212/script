#!/bin/bash
echo "=== SYSTEM INFO ==="
uname -a
echo
echo "=== CURRENT USER ==="
echo $USER
echo
echo "=== USERS WITH SHELL ==="
grep "sh$" /etc/passwd
echo
echo "=== NETWORK ==="
ip a | grep inet
echo
echo "=== PROCESSES ==="
ps aux
echo
echo "=== DISK USAGE ==="
df -h
echo
echo "=== OPEN PORTS ==="
ss -tuln
