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
        self.send("led r 255\r")
        self.send("led g 255\r")
        self.send("led b 255\r")
        self.send("led bl 255\r")
        self.send("power_otg 1\r")
        self.send("vibro 1\r")
        self.send("app_Music_Player\r")
        for i in range(3): 
            self.up()

    def powermin(self):
        self.main()
        self.send("vibro 0\r")
        self.send("led r 0\r")
        self.send("led g 0\r")
        self.send("led b 0\r")
        self.send("led bl 0\r")
        self.send("power_otg 0\r")

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
        self.send("app_125_kHz_RFID\r")
        time.sleep(2)
        self.back()
        self.send("app_GPIO\r")
        time.sleep(2)
        self.back()
        self.send("app_Infrared\r")
        time.sleep(2)
        self.back()
        self.send("app_Music_Player\r")
        time.sleep(2)
        self.back()
        self.send("app_NFC\r")
        time.sleep(2)
        self.back()
        self.send("app_Sub-GHz\r")
        time.sleep(2)
        self.back()
        self.send("app_iButton\r")
        time.sleep(2)
        self.back()
        time.sleep(2)