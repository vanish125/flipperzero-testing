#!/usr/bin/env python3
import os
import subprocess
import json

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



one_port_func = ('HeapTest',
                'PowerInfo',
                'BTcheck',
                'IntFree',
                'CryptoCheck'
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
