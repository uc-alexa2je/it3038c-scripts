#!/bin/bash

#This is a script that outputs the IP address and Hostname of a machine




a=$(ip a | grep 'noprefixroute ens192' | awk '{print $2}')
echo My IP is $a
