#!/usr/bin/env python3
import os
import subprocess
import argparse
from cgi import test
from numpy import void
from flipper.tests import tests
from flipper.serial import FlipperSerial
from flipper.serial import FlipperHEXKeyboard
from flipper.serial import FlipperTextKeyboard
from flipper.serial import ImageCompare
import serial
from orig.reference import Ref
from const import cnt
from const import f_dict
import time
import logging
import sys
from time import sleep
from datetime import datetime


class SupportFunction:

    def __init__(self):
        time.sleep(0.01)
    
    def main_back(self):
        port = self
        for i in range(5):
            port.key("SHORT BACK")
            sleep(1)
        
        sleep(1)
            
        
    def print_feedback(status, line):
        if status == 'try':
            print(line + (": correctly").rjust(60 - len(line)))
        elif status == 'false':
            print(line + (": error").rjust(60 - len(line)))


    def open_universal_lib(self):
        
        port = self
        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT OK')
        sleep(3)  #del magic 
    
    def button_press(self, data):
        
        number = data
        port = self
        port.key('SHORT DOWN')
        port.key('SHORT LEFT')
        port.key('SHORT LEFT')
        sleep(1)
        if number == cnt.MUTE: #mute_check
            port.key('SHORT UP')
            sleep(1)
            port.key('SHORT OK')
            sleep(3)
        elif number == cnt.VOL_UP: #volume_up_check
            port.key('SHORT RIGHT')
            port.key('SHORT OK')
        elif number == cnt.VOL_DOWN: #volume_down_check
            port.key('SHORT RIGHT')
            port.key('SHORT RIGHT')
            port.key('SHORT OK')
        elif number == cnt.CH_UP: #channel_up_check
            port.key('SHORT UP')
            port.key('SHORT RIGHT')
            port.key('SHORT OK')
        elif number == cnt.CH_DOWN: #chennel_down_check
            port.key('SHORT UP')
            port.key('SHORT RIGHT')
            port.key('SHORT RIGHT')
            port.key('SHORT OK')
        
        time.sleep(3)


    def check_correctness(button, data):
        button_type = (cnt.MUTE, cnt.VOL_UP, cnt.VOL_DOWN, cnt.CH_UP, cnt.CH_DOWN)
        button_name = ['MUTE', 'VOL_UP', 'VOL_DOWN', 'CH_UP', 'CH_DOWN']

        button_cod = {
            cnt.MUTE        : Ref.MUTE,
            cnt.VOL_UP      : Ref.VOLP,
            cnt.VOL_DOWN    : Ref.VOLM,
            cnt.CH_UP       : Ref.CHP,
            cnt.CH_DOWN     : Ref.CHM
        }
        

        if button in button_type:
            if data == button_cod[button]:
                SupportFunction.print_feedback('try', button_name[button])     
            else:
                SupportFunction.print_feedback('false', button_name[button])
                
    def open_learn_new_remote(self):
        port = self
        port.send('loader open "Infrared"')
        sleep(1)
        self.key('SHORT DOWN')
        self.key('SHORT OK')
    


    def learn_new_remote(port1, port2):
        port = port1
        portr = port2

        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.2)
        
        portr.send("ir tx Samsung32 0x0E 0x0C")
        sleep(2)
        portr.CTRLc()
        sleep(1)
        port.imageFile('Sams320E0C.png')
        sleep(1)

        if ImageCompare.compare('Sams320E0C.png') == None:
            port.key('SHORT RIGHT')
            keeb_hex = FlipperHEXKeyboard(port, "key")
            keeb_text = FlipperTextKeyboard(port, "key")
            keeb_text.send("qwerty9137___0000")
            feedback = 'signal received 1'
            SupportFunction.print_feedback('try', feedback)
            
        else:
            feedback = 'signal not received 1'
            SupportFunction.print_feedback('false', feedback)
            #error
            
        sleep(3)
        port.key('SHORT BACK')
        sleep(0.2)
        port.key('SHORT LEFT')
    
    def check_saved_remotes(port1, port2):
        port = port1
        portr = port2

        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        time.sleep(1)
        port.imageFile('EmptyFolder.png')
        time.sleep(1)
        
        if ImageCompare.compare('EmptyFolder.png') == None:
            sleep(1)
            feedback = 'signal wasn"t saved 1'
            SupportFunction.print_feedback('false', feedback)
            return 0
            
        else: 
            feedback = 'signal was saved 1'
            SupportFunction.print_feedback('try', feedback)
            return 1

    def add_button_to_remote(port1, port2):
        port = port1
        portr = port2
        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT RIGHT')
        port.key('SHORT OK')
        sleep(1)
        portr.send("ir tx Samsung32 0x0E 0x0C")
        portr.CTRLc()
        sleep(1)
        port.imageFile('Sams320E0C.png')
        sleep(1)
        if ImageCompare.compare('Sams320E0C.png') == None:
            port.key('SHORT RIGHT')
            keeb_hex = FlipperHEXKeyboard(port, "key")
            keeb_text = FlipperTextKeyboard(port, "key")
            keeb_text.send("key2")
            sleep(0.1)
            feedback = 'signal received 2'
            SupportFunction.print_feedback('try', feedback)
            return 1
        else:
            feedback = 'signal not received 2'
            SupportFunction.print_feedback('false', feedback)
            #error 
            time.sleep(0.1)
            port.key('SHORT BACK')
            return 0

    def add_button_to_remote_edit(port1, port2):
        port = port1
        portr = port2
        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT RIGHT')
        sleep(0.2)
        port.key('SHORT RIGHT')
        sleep(0.2)
        port.key('SHORT RIGHT')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.5)
        port.key('SHORT OK')
        sleep(1)
        portr.send("ir tx Samsung32 0x0E 0x0C")
        portr.CTRLc()
        sleep(1)
        port.imageFile('Sams320E0C.png')
        sleep(1)

        if ImageCompare.compare('Sams320E0C.png') == None:
            port.key('SHORT RIGHT')
            keeb_hex = FlipperHEXKeyboard(port, "key")
            keeb_text = FlipperTextKeyboard(port, "key")
            keeb_text.send("key3___asdfghjfghjkl")
            sleep(0.1)
            
            feedback = 'signal was created 1'
            SupportFunction.print_feedback('try', feedback)
            return 1
        else:
            feedback = 'signal wasn"t created 1'
            SupportFunction.print_feedback('false', feedback)
            #error 
            time.sleep(0.1)
            port.key('SHORT BACK')
            port.key('SHORT LEFT')
            return 0

    def rename_button_zero(port1, port2):
        port = port1
        portr = port2
        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.2)
        for i in range(4):
            port.key('SHORT RIGHT')
            sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.5)
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.5)
        port.key('SHORT UP')
        for i in range(22):
            port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        keeb_text = FlipperTextKeyboard(port, "key")
        keeb_text.send("000000000000000000000")
        sleep(3)
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        port.imageFile('ButtonZero.png')
        time.sleep(1)
        if ImageCompare.compare('ButtonZero.png') == None:
            port.key('SHORT RIGHT')
            feedback = 'Button was created correctly 1'
            SupportFunction.print_feedback('try', feedback)
            return 1
        else:
            feedback = 'Button wasn"t created correctly 1'
            SupportFunction.print_feedback('false', feedback)
            #error 
            port.key('SHORT RIGHT')
            return 0
    
    def rename_remote(port1, port2):
        port = port1
        portr = port2
        port.send('loader open Infrared')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(0.2)
        for i in range(3):
            port.key('SHORT RIGHT')
            sleep(0.2)
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.key('SHORT UP')
        for i in range(22):
            port.key('SHORT OK')
        sleep(1)
        port.key('SHORT DOWN')
        keeb_text = FlipperTextKeyboard(port, "key")
        keeb_text.send("111111111111111111111")
        sleep(3)
        port.key('SHORT OK')
        sleep(0.2)
        port.key('SHORT DOWN')
        sleep(0.2)
        port.key('SHORT OK')
        sleep(1)
        port.imageFile('Remote.png')
        time.sleep(1)
        if ImageCompare.compare('Remote.png') == None:
            port.key('SHORT RIGHT')
            feedback = 'Remote was created correctly 1'
            SupportFunction.print_feedback('try', feedback)
            return 1
        else:
            feedback = 'Remote wasn"t created correctly 1'
            SupportFunction.print_feedback('false', feedback)
            #error 
            port.key('SHORT RIGHT')
            return 0
        sleep(3)
    
    def open_GPIO(self):
        port = self
        port.send('loader open "GPIO"')
        sleep(1)
    
    def check_5v(self):
        port = self
        for i in range(2):
            sleep(0.2)
            port.key('SHORT DOWN')
        sleep(0.5)
        for i in range(3):
            port.key('SHORT RIGHT')
            sleep(0.5)
            port.key('SHORT LEFT')
        print('Hmmm...\n', 'Maybe try restarting it?\n', 'Joke)\n')
        for i in range(2):
            sleep(0.5)
            port.key('SHORT UP')
        sleep(0.5)
    
    def check_manual_control(self):
        port = self
        port.key('SHORT DOWN')
        sleep(0.5)
        port.key('SHORT OK')
        sleep(0.5)
        for i in range(10):
            port.key('LONG OK')
            port.key('SHORT RIGHT') 
            sleep(0.01)
        for i in range(10):
            port.key('LONG OK')
            port.key('SHORT LEFT')
            sleep(0.01)
        for i in range(10):
            port.send('input send ok press')
            if i in range(10):
                port.key('SHORT RIGHT')
        sleep(2)
        for i in range(10):
            port.key('SHORT LEFT')
            if i in range(10):
                port.key('SHORT OK')
        sleep(1)
        for i in range(2):
            port.key('SHORT BACK')
    
    def change_frequency(frequency, port1):
        f_dict = {'300': 0, '303.87': 1, '304.25': 2,     '310': 3,
                  '315': 4,    '318': 5,    '390': 6,     '418': 7, 
               '433.07': 8, '433.42': 9, '433.92': 10, '434.42': 11,
               '434.77': 12,'438.90': 13,'868.35': 14,    '915': 15,   
                  '925': 16,}

        port = port1
        port.key('SHORT LEFT')
        sleep(0.05)

        for i in range(16):
            port.key('SHORT LEFT')
            sleep(0.05)

        for i in range(f_dict[frequency]):
            port.key('SHORT RIGHT')
            sleep(0.05)

        port.key('SHORT BACK')
        sleep(0.05)
    
    def add_manually(port1, name_signal = 'Princeton_433', frequency = '433.92'):

        port = port1
        
        type_use_dict = (name_signal in f_dict.signal_dict)
        # True - use f_dict.signal_dict
        # False - use f_dict.fr_dict

        for i in range(3):
            port.key('SHORT DOWN')
            sleep(0.05)
        port.key('SHORT OK')
        sleep(0.05)

        if type_use_dict == True:
            for i in range(f_dict.signal_dict[name_signal]):
                port.key('SHORT DOWN')
                sleep(0.05)
            port.key('SHORT OK')
            sleep(0.05)
            keeb_text = FlipperTextKeyboard(port, "key")
            keeb_text.send(str(name_signal))
        elif type_use_dict == False:
            for i in range(f_dict.fr_dict[frequency]):
                port.key('SHORT DOWN')
                sleep(0.05)
            port.key('SHORT OK')
            sleep(0.05)
            keeb_text = FlipperTextKeyboard(port, "key")
            keeb_text.send(str(frequency))
        
        # add comp 
    

        port.key('SHORT OK')
        port.key('SHORT BACK')
        sleep(0.01)
        port.key('SHORT BACK')
        sleep(0.05)
        port.key('SHORT BACK')
        sleep(0.05)
        port.key('SHORT OK')
        sleep(0.05)

    def serial_number_file(port1, storage, file_name):
        #Use such names in "storage":   
        # badusb
        # irda
        # nfc
        # subghz
        # infrared
        # lfrfid
        # ibutton

        port = port1
        st_name = 'storage list /ext/'+storage
        
        data = FlipperSerial.send_and_wait_prompt(port,str(st_name))
        name = (' '+str(file_name))

        f_sym = data.find(name) 
        serial_number = data.count('\n', 0, f_sym)   
        return (serial_number - 1)





