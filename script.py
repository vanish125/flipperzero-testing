#!/usr/bin/env python3

from flipper.serial import FlipperSerial
from flipper.tests import tests
import logging
import argparse
import os
import sys
import subprocess
import time

BTstring = 'Ret: 0, HCI_Version: 11, HCI_Revision: 87, LMP_PAL_Version: 11, Manufacturer_Name: 48, LMP_PAL_Subversion: 8535\r\n'

class Main:
    def __init__(self):
        # logging
        self.logger = logging.getLogger()
        # command args
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-d", "--debug", action="store_true", help="Debug")
        self.parser.add_argument("-p", "--port", help="CDC Port", required=True)
        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.parser_cli = self.subparsers.add_parser("cli", help="Screen in cli")
        self.parser_cli.set_defaults(func=self.cli)
        self.parser_image = self.subparsers.add_parser("image", help="Make image screenshot")
        self.parser_image.add_argument("name", help="Name file")
        self.parser_image.set_defaults(func=self.image)
        self.parser_version = self.subparsers.add_parser("version", help="Version")
        self.parser_version.set_defaults(func=self.version)
        self.parser_PowerTest = self.subparsers.add_parser("PowerTest", help="PowerTest")
        self.parser_PowerTest.set_defaults(func=self.PowerTest)
        self.parser_HeapTest = self.subparsers.add_parser("HeapTest", help="HeapTest")
        self.parser_HeapTest.set_defaults(func=self.HeapTest)
        self.parser_PowerInfo = self.subparsers.add_parser("PowerInfo", help="PowerInfo")
        self.parser_PowerInfo.set_defaults(func=self.PowerInfo)
        self.parser_CheckOB = self.subparsers.add_parser("CheckOB", help="CheckOB")
        self.parser_CheckOB.set_defaults(func=self.CheckOB)
        self.parser_BTcheck = self.subparsers.add_parser("BTcheck", help="BTcheck")
        self.parser_BTcheck.set_defaults(func=self.BTcheck)
        self.parser_IntFree = self.subparsers.add_parser("IntFree", help="IntFree")
        self.parser_IntFree.set_defaults(func=self.IntFree)
        self.parser_ExitDFU = self.subparsers.add_parser("ExitDFU", help="ExitDFU")
        self.parser_ExitDFU.set_defaults(func=self.ExitDFU)
        self.parser_UsbTest = self.subparsers.add_parser("UsbTest", help="UsbTest")
        self.parser_UsbTest.set_defaults(func=self.UsbTest)




    def __call__(self):
        self.args = self.parser.parse_args()
        if "func" not in self.args:
            self.parser.error("Choose something to do")
        # configure log output
        self.log_level = logging.DEBUG if self.args.debug else logging.INFO
        self.logger.setLevel(self.log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setLevel(self.log_level)
        self.formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        # execute requested function
        self.args.func()

    def cli(self):
        subprocess.Popen(['python3', 'screen_stream.py', self.args.port])
        time.sleep(0.5)

    def image(self):
        self.imageFile(self.args.name)

    def imageFile(self, line):
        subprocess.Popen(['python3', 'screen.py', self.args.port, line])
        time.sleep(0.5)

    def CheckOB(self):
        subprocess.Popen(['python3', '../flipperzero-firmware/scripts/ob.py', 'check'])
        time.sleep(0.5)

    def ExitDFU(self):
        subprocess.Popen(['python3', 'pydfu.py', '-x'])
        time.sleep(0.5)

    def version(self):
        port = FlipperSerial(self.args.port)
        port.start()
        tests.Boot(port)
        self.imageFile('Boot.png')
        tests.FW(port)
        self.imageFile('FW.png')
        port.stop()

    def PowerTest(self):
        port = FlipperSerial(self.args.port)
        port.start()
        tests.powermax(port)
        time.sleep(3)
        tests.powermin(port)
        tests.PowerInfo(port)
        self.imageFile('Power.png')
        port.stop()

    def HeapTest(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("free")
        print('Clean:\r\n', data)
        tests.allapps(port)
        port.stop()
        port.start()
        data = port.send_and_wait_prompt("free")
        print('AllApps:\r\n', data)
        port.stop()

    def PowerInfo(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("power_info")
        print(data)
        port.stop()

    def BTcheck(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("bt_info")
        if data == BTstring:
            print(data)
        else: print('error\r')
        port.stop()

    def IntFree(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("storage info /int")
        print(data)
        port.stop()

    def IntFree(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("storage info /int")
        print(data)
        port.stop()

    def UsbTest(self):
        while(os.system(f'ls {self.args.port}')==0):          
          subprocess.Popen(['python3', 'reboot.py', self.args.port, 'dfu'])        
          time.sleep(1.5)
          self.ExitDFU()
          time.sleep(2)


if __name__ == "__main__":
    Main()()
