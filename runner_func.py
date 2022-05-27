#!/usr/bin/env python3
import os
import subprocess
import argparse
from flipper.serial import FlipperSerial
from orig.reference import Ref
from const import cnt
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
    
    def button_press(self, data):
        
        number = data
        port = self

        port.key('SHORT DOWN')
        port.key('SHORT LEFT')
        self.key('SHORT LEFT')

        if number == cnt.MUTE: #mute_check
            self.key('SHORT UP')
            self.key('SHORT OK')
        elif number == cnt.VOL_UP: #volume_up_check
            self.key('SHORT RIGHT')
            self.key('SHORT OK')
        elif number == cnt.VOL_DOWN: #volume_down_check
            self.key('SHORT RIGHT')
            self.key('SHORT RIGHT')
            self.key('SHORT OK')
        elif number == cnt.CH_UP: #channel_up_check
            self.key('SHORT UP')
            self.key('SHORT RIGHT')
            self.key('SHORT OK')
        elif number == cnt.CH_DOWN: #chennel_down_check
            self.key('SHORT UP')
            self.key('SHORT RIGHT')
            self.key('SHORT RIGHT')
            self.key('SHORT OK')
        
        time.sleep(3)


    def check_correctness(button, data):
        button_type = (cnt.MUTE, cnt.VOL_UP, cnt.VOL_DOWN, cnt.CH_UP, cnt.CH_DOWN)
        
        button_cod = {
            cnt.MUTE        : Ref.MUTE,
            cnt.VOL_UP      : Ref.VOLP,
            cnt.VOL_DOWN    : Ref.VOLM,
            cnt.CH_UP       : Ref.CHP,
            cnt.CH_DOWN     : Ref.CHM
        }

        if button in button_type:
            if data == button_cod[button]:
                return 'TRY'
            else:
                return 'FALSE'

    def open_learn_new_remote(self):
        self.main()
        self.send('loader open Infrared')
        self.key('SHORT DOWN')
        self.key('SHORT OK')
         

    def learn_new_remote(port1, port2):
        port = port1
        portr = port2

        
        SupportFunction.open_learn_new_remote(portr)
        SupportFunction.open_universal_lib(port)

        portr.send("ir rx")

        SupportFunction.button_press(port, cnt.MUTE)

        portr.CTRLc()
        data = portr.read_until_promp()
        print(data)
        response = SupportFunction.check_correctness(cnt.MUTE, data)
        print(response)
        data = ''
        time.sleep(0.1)


        SupportFunction.open_learn_new_remote(port)
        port.send("ir rx")
        portr.key('SHORT OK')
        time.sleep(0.1)
        port.CTRLc()
        data = port.read_until_promp()
        response = SupportFunction.check_correctness(cnt.MUTE, data)
        print(response)
        data = ''
        time.sleep(0.1)

        portr.send('SHORT RIGHT')

        




        

 
