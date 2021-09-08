#!/usr/bin/env python3

from flipper.storage import FlipperSerial
from flipper.storage import FlipperScreen
import logging
import argparse
import os
import sys
import binascii
import posixpath
from PIL import Image




class Main:

    def __init__(self):
        # command args
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-d", "--debug", action="store_true", help="Debug")
        self.parser.add_argument("-p", "--port", help="CDC Port", required=True)
        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.parser_mkdir = self.subparsers.add_parser("mkdir", help="Create directory")
        self.parser_mkdir.add_argument("flipper_path", help="Flipper path")
        self.parser_mkdir.set_defaults(func=self.mkdir)

        self.parser_remove = self.subparsers.add_parser(
            "remove", help="Remove file/directory"
        )
        self.parser_remove.add_argument("flipper_path", help="Flipper path")
        self.parser_remove.set_defaults(func=self.remove)

        self.parser_read = self.subparsers.add_parser("read", help="Read file")
        self.parser_read.add_argument("flipper_path", help="Flipper path")
        self.parser_read.set_defaults(func=self.read)

        self.parser_size = self.subparsers.add_parser("size", help="Size of file")
        self.parser_size.add_argument("flipper_path", help="Flipper path")
        self.parser_size.set_defaults(func=self.size)

        self.parser_receive = self.subparsers.add_parser("receive", help="Receive file")
        self.parser_receive.add_argument("flipper_path", help="Flipper path")
        self.parser_receive.add_argument("local_path", help="Local path")
        self.parser_receive.set_defaults(func=self.receive)

        self.parser_send = self.subparsers.add_parser(
            "send", help="Send file or directory"
        )
        self.parser_send.add_argument(
            "-f", "--force", help="Force sending", action="store_true"
        )
        self.parser_send.add_argument("local_path", help="Local path")
        self.parser_send.add_argument("flipper_path", help="Flipper path")
        self.parser_send.set_defaults(func=self.send)

        self.parser_list = self.subparsers.add_parser(
            "list", help="Recursively list files and dirs"
        )
        self.parser_list.add_argument("flipper_path", help="Flipper path", default="/")
        self.parser_list.set_defaults(func=self.list)

        # logging
        self.logger = logging.getLogger()

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
        
        
	def mkdir(self):
      	  serial = FlipperSerial(self.args.port)
        	serial.start()
        	self.logger.debug(f'Creating "{self.args.flipper_path}"')
        	if not serial.mkdir(self.args.flipper_path):
        	    self.logger.error(f"Error: {storage.last_error}")
       	 serial.stop()
       	 
       	 
       def cli(self):
        screen = FlipperScreen(self.args.port)
        screen.start()
        self.logger.debug(f'Screenshot in cli')
        x,y = screen.cli()
        if not data:
            self.logger.error(f"Error")
        else:
            try:
                print("Text data:")
                print(data.decode())
            except:
                print("Display:")
                for y in range(0, res_y, 2):
 	   		for x in range(1, res_x+1):
  	     	 if int(scr[x][y]) == 1 and int(scr[x][y+1]) == 1:
   	         print(u'\u2588', end='')
   	   	  if int(scr[x][y]) == 0 and int(scr[x][y+1]) == 1:
   	         print(u'\u2584', end='')
   	   	  if int(scr[x][y]) == 1 and int(scr[x][y+1]) == 0:
   	         print(u'\u2580', end='')
   	     	if int(scr[x][y]) == 0 and int(scr[x][y+1]) == 0:
   	         print(' ', end='')
   	 print()
        storage.stop()


    def image(self):
        screen = FlipperScreen(self.args.port)
        screen.start()
        self.logger.debug(f'Screenshot')
        res_x, res_y = screen.file(self.args.screen_path)
	im = Image.new('RGB', (res_x, res_y))
	im = Image.fromarray(img)
	im.save('screen.png')
	print('Saved to screen.png')
        storage.stop()




    def read(self):
        storage = FlipperStorage(self.args.port)
        storage.start()
        self.logger.debug(f'Reading "{self.args.flipper_path}"')
        data = storage.read_file(self.args.flipper_path)
        if not data:
            self.logger.error(f"Error: {storage.last_error}")
        else:
            try:
                print("Text data:")
                print(data.decode())
            except:
                print("Binary hexadecimal data:")
                print(binascii.hexlify(data).decode())
        storage.stop()

if __name__ == "__main__":
    Main()()
