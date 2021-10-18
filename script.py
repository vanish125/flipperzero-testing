#!/usr/bin/env python3

from flipper.serial import FlipperSerial
from flipper.screen import FlipperScreen
import logging
import argparse
import os
import sys
import binascii
import posixpath
from PIL import Image


class Main:
    def __init__(self):
        # logging
        self.logger = logging.getLogger()
        # command args
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-d", "--debug", action="store_true", help="Debug")
        self.parser.add_argument("-p", "--port", help="CDC Port", required=True)
        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.parser_cli = self.subparsers.add_parser("cli", help="Cli")
        self.parser_cli.set_defaults(func=self.cli)

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
        screen = FlipperScreen(self.args.port)
        screen.start()
        self.logger.debug(f"Screenshot in cli")
        x, y = screen.cli()
        if not data:
            self.logger.error(f"Error")
        else:
            try:
                print("Text data:")
                print(data.decode())
            except:
                print("Display:")
                for y in range(0, res_y, 2):
                    for x in range(1, res_x + 1):
                        if int(scr[x][y]) == 1 and int(scr[x][y + 1]) == 1:
                            print("\u2588", end="")
                        if int(scr[x][y]) == 0 and int(scr[x][y + 1]) == 1:
                            print("\u2584", end="")
                        if int(scr[x][y]) == 1 and int(scr[x][y + 1]) == 0:
                            print("\u2580", end="")
                        if int(scr[x][y]) == 0 and int(scr[x][y + 1]) == 0:
                            print(" ", end="")
                    print()
        storage.stop()

    def image(self):
        screen = FlipperScreen(self.args.port)
        screen.start()
        self.logger.debug(f"Screenshot")
        res_x, res_y = screen.file(self.args.screen_path)
        im = Image.new("RGB", (res_x, res_y))
        im = Image.fromarray(img)
        im.save("screen.png")
        print("Saved to screen.png")
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
