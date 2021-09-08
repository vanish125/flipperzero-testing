#!/usr/bin/env python3

# -*- coding: utf-8 -*- 

import sys
import serial

import numpy



class FlipperSerial:
    CLI_PROMPT = ">: "
    CLI_EOL = "\r\n"
    res_x = 128
    res_y = 64

    def __init__(self, portname: str):
        self.port = serial.Serial()
        self.port.port = portname
        self.port.timeout = 2
        self.port.baudrate = 115200
        self.read = BufferedRead(self.port)
        self.last_error = ""


    def start(self):
        self.port.open()
        self.port.reset_input_buffer()
        # Send a command with a known syntax to make sure the buffer is flushed
        self.send("device_info\r")
        self.read.until("hardware_model      :")
        # And read buffer until we get prompt
        self.read.until(self.CLI_PROMPT)

    def stop(self):
        self.port.close()

    def cli(self):
        self.port.write(b"\nscreen_stream\r\n")   #once
        self.port.read_until(bytes.fromhex('F0E1D2C3'))
        data = self.port.read(int(res_x*res_y/8))

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

	return(x,y)


    def file(self):
        self.port.write(b"\nscreen_stream\r\n")   #once
        self.port.read_until(bytes.fromhex('F0E1D2C3'))
        data = self.port.read(int(res_x*res_y/8))

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
	
	return (res_x, res_y)
