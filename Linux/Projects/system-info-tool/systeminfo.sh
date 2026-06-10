#!/bin/bash

echo "--------------------"
echo "SYSTEM INFORMATION"
echo "--------------------"

echo ""

echo "Current User:"
whoami

echo ""

echo "Current Date:"
date

echo ""

echo "Current Directory:"
pwd

echo ""

echo "Hostname:"
hostname

echo ""

echo "Operating System:"
uname -a

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Memory Usage:"
free -h
