#!/usr/bin/env python3

from cgi import test
from numpy import void
from flipper.serial import FlipperSerial
from flipper.serial import ImageCompare
from flipper.tests import tests
from runner_func import SupportFunction #support function

from orig.reference import Ref
from const import cnt
import logging
import argparse
import os
import sys
import subprocess
from time import sleep
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
        self.parser.add_argument("-r", "--portref", help="CDC Port Ref")
        self.subparsers = self.parser.add_subparsers(help="sub-command help")

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
        self.parser_RPCTest = self.subparsers.add_parser("RPCTest", help="RPCTest")
        self.parser_RPCTest.set_defaults(func=self.RPCTest)
        self.parser_NfcTest = self.subparsers.add_parser("NfcTest", help="NfcTest")
        self.parser_NfcTest.set_defaults(func=self.NfcTest)
        self.parser_RfidTest = self.subparsers.add_parser("RfidTest", help="RfidTest")
        self.parser_RfidTest.set_defaults(func=self.RfidTest)
        self.parser_iKeyTest = self.subparsers.add_parser("iKeyTest", help="iKeyTest")
        self.parser_iKeyTest.set_defaults(func=self.iKeyTest)
        self.parser_IrTest = self.subparsers.add_parser("IrTest", help="IrTest")
        self.parser_IrTest.set_defaults(func=self.IrTest)
        self.parser_CryptoCheck = self.subparsers.add_parser("CryptoCheck", help="CryptoCheck")
        self.parser_CryptoCheck.set_defaults(func=self.CryptoCheck)
        self.parser_SubGhzTest = self.subparsers.add_parser("SubGhzTest", help="SubGhzTest")
        self.parser_SubGhzTest.set_defaults(func=self.SubGhzTest)
        self.parser_RfidGuiTest = self.subparsers.add_parser("RfidGuiTest", help="RfidGuiTest")
        self.parser_RfidGuiTest.set_defaults(func=self.RfidGuiTest)

        self.parser_IrTestGui = self.subparsers.add_parser("IrTestGui", help="IrTestGui")
        self.parser_IrTestGui.set_defaults(func=self.IrTestGui)
        self.parser_GPIOGui = self.subparsers.add_parser("GPIOGui", help="GPIOGui")
        self.parser_GPIOGui.set_defaults(func=self.GPIOGui)
        self.parser_SubGHzTestGui = self.subparsers.add_parser("SubGHzTestGui", help="SubGHzTestGui")
        self.parser_SubGHzTestGui.set_defaults(func=self.SubGHzTestGui)

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
        print("Start testing")
        self.args.func()
        

    def image(self):
        self.imageFile(self.args.name)
    

    def imageFile(self, line):
        port = FlipperSerial(self.args.port)
        port.start()
        port.imageFile(line)
        port.stop()
        sleep(0.5)

    def CheckOB(self):
        subprocess.Popen(
            ['python3', '../flipperzero-firmware/scripts/ob.py', 'check'])
        sleep(0.5)

    def ExitDFU(self):
        subprocess.Popen(['python3', 'pydfu.py', '-x'])
        sleep(0.5)

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
        sleep(3)
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

    def RPCTest(self):
        ATTEMPT = 0
        port = FlipperSerial(self.args.port)
        data = data_o = "start_rpc_session"
        while(1):
            if (data == data_o):
              print("                                                              ",end="\r", flush=True)
              print("Port opened!", end="\r", flush=True)
              port.start()
              data = port.RPC_start()
              print(data)
              sleep(1)
              port.RPC_stop()
              print('Session terminated\r')
              port.stop()  
              sleep(1)
            else:
              ATTEMPT += 1
              print("Port no found for " + str(ATTEMPT) + " sec.",end="\r", flush=True)
            sleep(1)
        port.stop()    


    def UsbTest(self):
        ATTEMPT = 0
        START_DATE = str(datenow().strftime("%d/%m/%Y %H:%M:%S"))
        print("Run at: " + START_DATE)
        while(1):
            if (os.system(f'ls {self.args.port}')==0):
              print("                                                              ",end="\r", flush=True)
              print("Port opened!", end="\r", flush=True)
              subprocess.Popen(['python3', 'reboot.py', self.args.port, 'dfu'])
              sleep(1.5)
              self.ExitDFU()
              sleep(2)
              ATTEMPT = 0
            else:
              ATTEMPT += 1
              print("Port no found for " + str(ATTEMPT) + " sec.",end="\r", flush=True)
            sleep(1)

    def NfcTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        datar = portr.send_and_wait_ctrl("nfc emulate")
        sleep(1.5)
        data = port.send_and_wait_prompt("nfc detect")
        portr.CTRLc()
        #print(repr(data))
        if data == Ref.Nfc:
            print('Ok')
        else: print('Fail')
        portr.stop()
        port.stop()

    def RfidTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        datar = portr.send_and_wait_ctrl("rfid emulate EM4100 DC69660F12")
        sleep(1)
        data = port.send_and_wait_prompt("rfid read")
        portr.CTRLc()
        datar = portr.send_and_wait_ctrl("rfid emulate H10301 F4DBAC")  
        sleep(1)
        data = port.send_and_wait_prompt("rfid read") + data
        portr.CTRLc()
        datar = portr.send_and_wait_ctrl("rfid emulate I40134 B82191")
        sleep(1)
        data = port.send_and_wait_prompt("rfid read") + data
        portr.CTRLc()
        # print(repr(data))
        if data == Ref.Lfrfid:
            print('Ok')
        else: print('Fail')
        portr.stop()
        port.stop()

    def iKeyTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        datar = portr.send_and_wait_ctrl("ikey emulate Dallas 01F637C0010000BA")
        sleep(1)
        data = port.send_and_wait_prompt("ikey read")
        portr.CTRLc()
        datar = portr.send_and_wait_ctrl("ikey emulate Cyfral CEA3")
        sleep(1)
        data = port.send_and_wait_prompt("ikey read") + data
        portr.CTRLc()
        datar = portr.send_and_wait_ctrl("ikey emulate Metakom 8EC04BB2")
        sleep(1)
        data = port.send_and_wait_prompt("ikey read") + data
        portr.CTRLc()
        #print(repr(data))
        if data == Ref.iKey:
            print('Ok')
        else: print('Fail')
        portr.stop()
        port.stop()

    def IrTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        void = port.send("ir rx")
        sleep(1)
        datar = portr.send_and_wait_prompt("ir tx Samsung32 0x0E 0x0C")
        sleep(1)
        datar = portr.send_and_wait_prompt("ir tx RC5 0x04 0x2E")
        sleep(1)
        datar = portr.send_and_wait_prompt("ir tx NEC 0x04 0xD1")
        sleep(1)
        port.CTRLc()
        sleep(0.1)
        data = port.read_until_promp()
        #print(repr(data))
        if data == Ref.ir:
            print('Ok')
        else: print('Fail')
        portr.stop()
        port.stop()

    def CryptoCheck(self):
        port = FlipperSerial(self.args.port)
        port.start()
        port.send_and_wait_eol("crypto decrypt 1 cdf1298be4de2ad417fd24ae38537f7b")
        sleep(1)
        port.send_and_wait_eol("ebc4c98c04abe19eee1c2885cd7a2d22881a1d2235facc71598b39f7f7b31d69")
        sleep(1)
        port.CTRLc()
        sleep(0.1)
        data = port.read_until_promp()
        print(data)
        port.stop()


    def SubGhzTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        port.send("subghz rx 433920000")
        sleep(1)
        portr.send_and_wait_prompt("subghz tx 74bada 433920000 10")
        sleep(1)
        port.CTRLc()
        sleep(0.1)
        data = port.read_until_promp()
        sleep(0.1)
        port.send("subghz rx 315000000")
        sleep(1)
        portr.send_and_wait_prompt("subghz tx 74badb 315000000 10")
        sleep(1)
        port.CTRLc()
        sleep(0.1)
        data = port.read_until_promp() + data
        sleep(0.1)
        port.send("subghz rx 868350000")
        sleep(1)
        portr.send_and_wait_prompt("subghz tx 74badc 868350000 10")
        sleep(1)
        port.CTRLc()
        sleep(0.1)
        data = port.read_until_promp() +data
        sleep(0.1)
        #print(repr(data))
        if data == Ref.SubGhz:
            print('Ok')
        else: print('Fail')
        portr.stop()
        port.stop()

    def IrTestGui(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        SupportFunction.open_universal_lib(port)

        num = (cnt.MUTE, cnt.VOL_UP, cnt.VOL_DOWN, cnt.CH_UP, cnt.CH_DOWN)
        
        for nextb in num: 
            void = portr.send("ir rx")
            sleep(1)
            SupportFunction.button_press(port, nextb)
            sleep(1)
            portr.CTRLc()
            data = portr.read_until_promp()
            SupportFunction.check_correctness(nextb, data)
            data = ''
        
        SupportFunction.main_back(port)

        SupportFunction.learn_new_remote(port, portr)
        SupportFunction.main_back(port)  
        feedback = SupportFunction.check_saved_remotes(port, portr)
        if feedback == 1:
            SupportFunction.main_back(port)
            feedback = SupportFunction.add_button_to_remote(port, portr)
            if feedback == 1:
                SupportFunction.main_back(port)
                feedback = SupportFunction.add_button_to_remote_edit(port, portr)
                if feedback == 1:
                    SupportFunction.main_back(port)
                    feedback = SupportFunction.rename_button_zero(port, portr)
                    if feedback == 1:
                        SupportFunction.main_back(port)
                        feedback = SupportFunction.rename_remote(port, portr)
                        if feedback == 1:
                            feedback = 'All test'
                            SupportFunction.print_feedback('try', feedback)
                            SupportFunction.main_back(port)
                    elif feedback == 0:
                        SupportFunction.main_back(port)
                        feedback = 'All test'
                        SupportFunction.print_feedback('false', feedback)
                elif feedback == 0:
                    SupportFunction.main_back(port)
                    feedback = 'All test'
                    SupportFunction.print_feedback('false', feedback)
            elif feedback == 0:
                SupportFunction.main_back(port)
                feedback = 'All test'
                SupportFunction.print_feedback('false', feedback)
        elif feedback == 0:
            SupportFunction.main_back(port)
            feedback = 'All test'
            SupportFunction.print_feedback('false', feedback) 

        print('End of testing')
        portr.stop()
        port.stop()
    
    def SubGHzTestGui(self):
        port = FlipperSerial(self.args.port)
        port.start()
        serial_number = SupportFunction.serial_number_file(port, 'subghz', 'Gate_TX_433.sub')
        print(serial_number)
        SupportFunction.add_manually(port, 'Gate_TX_433')
        
        port.stop()
    
    def GPIOGui(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        portr.start()
        port.start()
        SupportFunction.open_GPIO(port)
        SupportFunction.check_5v(port)
        SupportFunction.check_manual_control(port)
        print('End of testing')
        portr.stop()
        port.stop()

    
    def RfidGuiTest(self):
        port = FlipperSerial(self.args.port)
        portr = FlipperSerial(self.args.portref)
        port.start()
        portr.start()
        tests.lfrfid_em_create(port)
        data = portr.send_and_wait_prompt("rfid read")
        sleep(1)
        port.imageFile('EmRFID1.png')
        tests.lfrfid_hid_create(port)
        data = portr.send_and_wait_prompt("rfid read") + data
        sleep(1)
        port.imageFile('EmRFID2.png')
        tests.lfrfid_indala_create(port)
        data = portr.send_and_wait_prompt("rfid read") + data
        sleep(1)
        port.imageFile('EmRFID3.png')
        port.main()
        # print(repr(data))
        if ImageCompare.compare('EmRFID1.png') == None and ImageCompare.compare('EmRFID2.png') == None and ImageCompare.compare('EmRFID3.png') == None and data == Ref.Lfrfid:
            print('Ok')
        else: print('Fail')
        portr.send_and_wait_ctrl("rfid emulate EM4100 DC69660F12")
        tests.lfrfid_read_and_save(port)
        portr.CTRLc()
        port.imageFile('EmRFID4.png')
        data = portr.send_and_wait_prompt("rfid read")
        # print(repr(data))
        if ImageCompare.compare('EmRFID4.png') == None and data == 'd\r\nReading RFID...\r\nPress Ctrl+C to abort\r\nEM4100 DC69660F12\r\nReading stopped\r\n\r\n':
            print('Ok')
        else: print('Fail')
        port.main()
        port.stop()
        portr.stop()

if __name__ == "__main__":
    Main()()
