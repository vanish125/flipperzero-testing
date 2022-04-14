#!/usr/bin/env python3

from flipper.serial import FlipperSerial
from flipper.tests import tests
import logging
import argparse
import os
import sys
import subprocess
import time
from datetime import datetime

BTstring = 'Ret: 0, HCI_Version: 11, HCI_Revision: 87, LMP_PAL_Version: 11, Manufacturer_Name: 48, LMP_PAL_Subversion: 8535\n\r'


class Main:
    def __init__(self):
        # logging
        self.logger = logging.getLogger()
        # command args
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-d", "--debug", action="store_true", help="Debug")
        self.parser.add_argument("-p", "--port", help="CDC Port", required=True)
        self.parser.add_argument("-pr", "--portref", help="CDC Port Ref")
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
        self.parser_Test = self.subparsers.add_parser("Test", help="TestFW")
        self.parser_Test.set_defaults(func=self.Test)
        self.parser_RPSTest = self.subparsers.add_parser("RPSTest", help="RPSTest")
        self.parser_RPSTest.set_defaults(func=self.RPSTest)
        self.parser_NfcTest = self.subparsers.add_parser("NfcTest", help="NfcTest")
        self.parser_NfcTest.set_defaults(func=self.NfcTest)
        self.parser_RfidTest = self.subparsers.add_parser("RfidTest", help="RfidTest")
        self.parser_RfidTest.set_defaults(func=self.RfidTest)

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
        subprocess.Popen(
            ['python3', '../flipperzero-firmware/scripts/ob.py', 'check'])
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
        data = port.send_and_wait_prompt("power info")
        print(data)
        port.stop()

    def BTcheck(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("bt hci_info")
        if data == BTstring:
            print(data)
        else:
            print(data)
            print('error\r')
        port.stop()

    def IntFree(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("storage info /int")
        print(data)
        port.stop()

    def ExtFree(self):
        port = FlipperSerial(self.args.port)
        port.start()
        data = port.send_and_wait_prompt("storage info /ext")
        print(data)
        port.stop()

    def Test(self):
        port = FlipperSerial(self.args.port)
        port.start()
        print('Press "Ctrl + c" to stop testing')
        try:
            while True:
                tests.allapps(port)
        except KeyboardInterrupt:
            pass
        port.stop()

    def RPSTest(self):
        ATTEMPT = 0
        port = FlipperSerial(self.args.port)
        data = data_o = "start_rpc_session"
        while(1):
            if (data == data_o):
              print("                                                              ",end="\r", flush=True)
              print("Port opened!", end="\r", flush=True)
              port.start()
              data = port.send_and_wait_eol("start_rpc_session")
              print(data)
              time.sleep(2)
              port.RPS_stop
              print('Session terminated\r')
              port.stop()  
              time.sleep(2)
            else:
              ATTEMPT += 1
              print("Port no found for " + str(ATTEMPT) + " sec.",end="\r", flush=True)
            time.sleep(1)
        port.stop()    


    def UsbTest(self):
        ATTEMPT = 0
        START_DATE = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("Run at: " + START_DATE)
        while(1):
            if (os.system(f'ls {self.args.port}')==0):
              print("                                                              ",end="\r", flush=True)
              print("Port opened!", end="\r", flush=True)
              subprocess.Popen(['python3', 'reboot.py', self.args.port, 'dfu'])
              time.sleep(1.5)
              self.ExitDFU()
              time.sleep(2)
              ATTEMPT = 0
            else:
              ATTEMPT += 1
              print("Port no found for " + str(ATTEMPT) + " sec.",end="\r", flush=True)
            time.sleep(1)

    def NfcTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        datar = portr.send_and_wait_ctrl("nfc emulate")
        time.sleep(1.5)
        data = port.send_and_wait_prompt("nfc detect")
        portr.CTRLc()
        print(data)
        portr.stop()
        port.stop()

    def RfidTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        datar = portr.send_and_wait_ctrl("rfid emulate H10301 F4DBAC")
        time.sleep(1)
        data = port.send_and_wait_prompt("rfid read")
        portr.CTRLc()
        print(data)
        datar = portr.send_and_wait_ctrl("rfid emulate EM4100 DC69660F12")
        time.sleep(1)
        data = port.send_and_wait_prompt("rfid read")
        portr.CTRLc()
        print(data)
        datar = portr.send_and_wait_ctrl("rfid emulate I40134 B82191")
        time.sleep(1)
        data = port.send_and_wait_prompt("rfid read")
        portr.CTRLc()
        print(data)
        portr.stop()
        port.stop()

if __name__ == "__main__":
    Main()()
