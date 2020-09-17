#!/bin/sh
date +%F-%T >> /var/log/epson.log
cd /home/francisco/PrinterTpvBelleza
python3 /home/francisco/PrinterTpvBelleza/printer_web.py >> /var/log/epson.log  2>&1 
date +%F-%T >> /var/log/epson.log
