#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

import sys
import serial

import numpy

from PIL import Image

import importlib

protoflipper_module = importlib.import_module(
    "flipperzero-protobuf-py.flipper_protobuf")

image_path = "out"

res_x = 128
res_y = 64
name = sys.argv[2]


def main():
    # open serial port
    flipper = serial.Serial(sys.argv[1], timeout=1)
    flipper.baudrate = 230400
    flipper.flushOutput()
    flipper.flushInput()
    flipper.timeout = None
    flipper.read_until(b'>: ')
    flipper.write(b"start_rpc_session\r")
    flipper.read_until(b'\n')


    proto = protoflipper_module.ProtoFlipper(flipper)


    data = proto.cmd_gui_snapshot_screen()

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

    #export to image file:

    scale = 3
    col_black = [0x11, 0x11, 0x11]
    col_white = [0xff, 0x8c, 0x29]
    col_bg = col_black

    img = numpy.zeros((res_y*scale, res_x*scale, 3), dtype=numpy.uint8)
    for y in range(0, res_y*scale):
        for x in range(0, res_x*scale):
            img[y][x] = col_bg

    for y in range(0, res_y):
        for x in range(1, res_x+1):
            if int(scr[x][y]) == 1:
                for yy in range(y*scale, (y+1)*scale):
                    for xx in range((x-1)*scale, x*scale):
                        img[yy][xx] = col_black
            else:
                for yy in range(y*scale, (y+1)*scale):
                    for xx in range((x-1)*scale, x*scale):
                        img[yy][xx] = col_white
                        #img[y*scale][(x-1)*scale] = col_white

    im = Image.new('RGB', (res_x, res_y))
    im = Image.fromarray(img)
    im.save(f'{image_path}/{name}')

    print('Saved to', name)


if __name__ == '__main__':
    main()
