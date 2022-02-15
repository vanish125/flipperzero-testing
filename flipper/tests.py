from .serial import FlipperSerial
import time


class tests:

    def FW(self):
        self.main()
        self.ldown()

    def Boot(self):
        self.main()
        self.ldown()
        self.down()

    def powermax(self):
        self.main()
        self.send("led r 255")
        self.send("led g 255")
        self.send("led b 255")
        self.send("led bl 255")
        self.send("power_otg 1")
        self.send("vibro 1")
        self.send("loader open Music Player")
        for i in range(3): 
            self.up()

    def powermin(self):
        self.main()
        self.send("vibro 0")
        self.send("led r 0")
        self.send("led g 0")
        self.send("led b 0")
        self.send("led bl 0")
        self.send("power_otg 0")

    def PowerInfo(self):
        self.main()
        self.ok()
        self.up() 
        self.ok()
        for i in range(3): 
            self.down()
        self.ok()
        self.ok()

    def allapps(self):
        self.main()
        self.send("loader open 125 kHz RFID")
        time.sleep(1)
        self.back()
        self.send("loader open GPIO")
        time.sleep(1)
        self.back()
        self.send("loader open Infrared")
        time.sleep(1)
        self.back()
        self.send("loader open Music Player")
        time.sleep(1)
        self.back()
        self.send("loader open NFC")
        time.sleep(1)
        self.back()
        self.send("loader open Sub-GHz")
        time.sleep(1)
        self.back()
        self.send("loader open iButton")
        time.sleep(1)
        self.back()
        time.sleep(1)