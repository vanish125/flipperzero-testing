#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

import sys
import serial


type = sys.argv[2]

ser = serial.Serial(sys.argv[1])
ser.baudrate = 230400

if type=='dfu':
  ser.write(b"\ndfu\r\n")

if type=='reboot':
  ser.write(b"\nreboot\r\n")