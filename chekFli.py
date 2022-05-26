#!/usr/bin/env python3
import os
import subprocess
import json
import argparse


class Main:

    def __init__(self):
        # command args
        self.parser = argparse.ArgumentParser()

        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.parser_test = self.subparsers.add_parser("test", help="test help")
        self.parser_test.set_defaults(func=self.test)
    
        self.parser_full = self.subparsers.add_parser("full", help="full help")
        self.parser_full.set_defaults(func=self.Full)

    def __call__(self):
        self.args = self.parser.parse_args()
        if "func" not in self.args:
            self.parser.error("Choose something to do")
        # execute requested function
        print("Start testing")
        self.args.func()

    def test(self):
        print("Start2")
        test = 'PowerTest'
        feed_back = subprocess.run(
                ['python3', './script.py', '-p/dev/ttyACM0', '-r/dev/ttyACM1', test])

    def Full(self):

        tempdir = "out/"
        filelist = [ f for f in os.listdir(tempdir)]
        for f in filelist:
            os.remove(os.path.join(tempdir, f))
        if (os.path.isfile('./test_log.txt') == True):
            os.remove("test_log.txt")
        if (os.path.isfile('./test_log.json') == True):
            os.remove("test_log.json")

        log_txt = open("test_log.txt", "a+")
        log_json = open('test_log.json', 'a+')

        # --------------------dual port feature testing------------------------
        two_port_func = ('NfcTest',
                        'RfidTest',
                        'iKeyTest',
                        'IrTest',
                        )

        for test in two_port_func:

            feed_back = subprocess.run(
                ['python3', './script.py', '-p/dev/ttyACM0', '-r/dev/ttyACM1', test])
            
            json_data = {'Test:' : test, 'Returncode - ': feed_back.returncode}   
            log_json.write(json.dumps(json_data))
            
            log_json.write('\n')


            log_txt.write(str(feed_back))
            log_txt.write('\n')

            feed_back = 1



        # --------------------one port feature testing------------------------
        # 'UsbTest',
        #'CheckOB' -st ,
        # 'IntFree',
        # 'RPSTest',
        #



        one_port_func = ('HeapTest',
                        'PowerInfo',
                        'BTcheck',
                        'IntFree',
                        'CryptoCheck',
                        'PowerTest'
                        )


        for test in one_port_func:

            feed_back = subprocess.run(['python3', './script.py', '-p/dev/ttyACM0', test])

            json_data = {'Test:' : test, 'Returncode - ': feed_back.returncode}   
            log_json.write(json.dumps(json_data))
            log_json.write('\n')

            log_txt.write(str(feed_back))
            log_txt.write('\n')

            feed_back = 1
            
        log_txt.close()
        log_json.close()

if __name__ == "__main__":
    Main()()