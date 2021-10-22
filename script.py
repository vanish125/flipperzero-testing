#!/usr/bin/env python3

from flipper.serial import FlipperSerial
from flipper.tests import tests
import logging
import argparse
import os
import sys
import binascii
import posixpath
import subprocess
import time


class Main:
    def __init__(self):
        # logging
        self.logger = logging.getLogger()
        # command args
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            "-d", "--debug", action="store_true", help="Debug")
        self.parser.add_argument(
            "-p", "--port", help="CDC Port", required=True)
        self.subparsers = self.parser.add_subparsers(help="sub-command help")

        self.parser_cli = self.subparsers.add_parser(
            "cli", help="Screen in cli")
        self.parser_cli.set_defaults(func=self.cli)

        self.parser_image = self.subparsers.add_parser(
            "image", help="Make image screenshot")
        self.parser_image.set_defaults(func=self.image)

        self.parser_test = self.subparsers.add_parser("test", help="Test HW")
        self.parser_test.set_defaults(func=self.test)

    def __call__(self):
        self.args = self.parser.parse_args()
        if "func" not in self.args:
            self.parser.error("Choose something to do")
        # configure log output
        self.log_level = logging.DEBUG if self.args.debug else logging.INFO
        self.logger.setLevel(self.log_level)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setLevel(self.log_level)
        self.formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s")
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        # execute requested function
        self.args.func()

    def cli(self):
        subprocess.Popen(['python3', 'screen_stream.py', self.args.port])

    def image(self):
        self.imageFile('screen.png')

    def imageFile(self, line):
        subprocess.Popen(['python3', 'screen.py', self.args.port, line])

    def test(self):
        tests.test(self)
        self.imageFile('test.png')


if __name__ == "__main__":
    Main()()
