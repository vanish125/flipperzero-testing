#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

import sys
import serial

import numpy

res_x = 128
res_y = 64
n = 0

ser = serial.Serial(sys.argv[1])
ser.write(b"\nscreen_stream\r")   #once
while n == 0:
    ser.read_until(bytes.fromhex('F0E1D2C3'))
    data = ser.read(int(res_x*res_y/8))

    get_bin = lambda x: format(x, 'b')

    scr = numpy.zeros((res_x+1, res_y+1))

    x = y = 0
    basey = 0

    for i in range(0, int(res_x*res_y/8)):
        tmp = get_bin(data[i])
        tmp = '0'*(8-len(tmp)) + tmp
        tmp = tmp[::-1]     #reverse
        
        y = basey
        x += 1
        for c in tmp:
            scr[x][y] = c
            y += 1
        
        if (i + 1) % res_x == 0:
            basey += 8
            x = 0

    print(chr(27) + "[2H")
    for y in range(0, res_y, 2):
        for x in range(1, res_x+1):
            if int(scr[x][y]) == 1 and int(scr[x][y+1]) == 1:
                print(u'\u2588', end='')
            if int(scr[x][y]) == 0 and int(scr[x][y+1]) == 1:
                print(u'\u2584', end='')
            if int(scr[x][y]) == 1 and int(scr[x][y+1]) == 0:
                print(u'\u2580', end='')
            if int(scr[x][y]) == 0 and int(scr[x][y+1]) == 0:
                print(' ', end='')
        print()
    n = 1

