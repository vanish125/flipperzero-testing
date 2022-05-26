#!/usr/bin/env python3
import os
import subprocess
import argparse
from flipper.serial import FlipperSerial
import time


class SupportFunction:

    def __init__(self):
        time.sleep(0.01)
    
    def open_universal_lib(self):
        self.main()
        self.send('loader open Infrared')
        self.key('SHORT OK')
        self.key('SHORT OK')
        time.sleep(4)  #del magic 

    def mute_check(self):
        self.key('SHORT UP')
        self.key('SHORT OK')
        time.sleep(3)
        
    def check_correctness(self, line):
        botton_type = ['POWER', 'VOL+', 'VOL-', 'CH+', 'CH-', 'MUTE']
        botton = line

        #for botton in botton_type:
        #    if botton == botton_type


        botton_cod = {
            '': 10,
            '': 1
        }


        # self.key('SHORT DOWN')
        # self.key('SHORT OK')
        # self.key('SHORT LEFT')
        # self.key('SHORT OK')
        # self.key('SHORT UP')
        # self.key("SHORT RIGHT")
        # for i in range(5): 
            # self.key("SHORT RIGHT")
        # time.sleep(1.5)
        # self.send('loader open "Music Player"')
 