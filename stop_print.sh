#!/bin/bash

getpid=$(ps aux -O start | grep -i "printer_web.py" | grep -v grep | grep -v "stop_print.sh" | awk '{ if (NR==1) {print $2}}')
echo $getpid
kill -9 $getpid
