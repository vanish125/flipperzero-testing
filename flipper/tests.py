from .serial import FlipperSerial
import time

class tests:
    def test(self):
        test = FlipperSerial(self.args.port)
        test.start()
        test.ok()       
        test.back()
        test.stop()
