#!/bin/bash

echo "---------------------------------"
echo "NETWORK INFORMATION REPORT"
echo "---------------------------------"

echo ""
echo "Hostname:"
hostname

echo ""
echo "Local IP Address:"
hostname -I

echo ""
echo "Default Gateway:"
ip route | grep default

echo ""
echo "Open Listening Ports:"
ss -tuln

echo ""
echo "Date:"
date

echo ""
echo "DNS Servers:"
cat /etc/resolv.conf | grep nameserver

echo ""
echo "Network Interfaces:"
ip addr show
