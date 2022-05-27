from .serial import FlipperSerial
from .serial import FlipperHEXKeyboard
from .serial import FlipperTextKeyboard
from time import sleep

class tests:

    def FW(self):
        self.main()
        self.key('LONG DOWN')

    def Boot(self):
        self.main()
        self.key('LONG DOWN')
        self.key('SHORT DOWN')

    def powermax(self):
        self.main()
        self.send('led r 255')
        self.send('led g 255')
        self.send('led b 255')
        self.send('led bl 255')
        self.send('power 5v 1')
        self.send('vibro 1')
        self.send('loader open "Music Player"')
        for i in range(3): 
            self.key('SHORT UP')

    def powermin(self):
        self.main()
        self.send('vibro 0')
        self.send('led r 0')
        self.send('led g 0')
        self.send('led b 0')
        self.send('led bl 0')
        self.send('power_otg 0')

    def PowerInfo(self):
        self.main()
        self.key('SHORT OK')
        self.key('SHORT UP')
        self.key('SHORT OK')
        for i in range(3): 
            self.key('SHORT DOWN')
        self.key('SHORT OK')
        self.key('SHORT OK')

    def allapps(self):
        self.main()
        self.send('loader open "125 kHz RFID"')
        sleep(1)
        self.key('SHORT BACK')
        self.send('loader open "GPIO"')
        sleep(1)
        self.key('SHORT BACK')
        self.send('loader open "Infrared"')
        sleep(1)
        self.key('SHORT BACK')
        self.send('loader open "Music Player"')
        sleep(1)
        self.key('SHORT BACK')
        self.send('loader open "NFC"')
        sleep(1)
        self.key('SHORT BACK')
        self.send('loader open "Sub-GHz"')
        sleep(1)
        self.key('SHORT BACK')
        self.send('loader open "iButton"')
        sleep(1)
        self.key('SHORT BACK')
        sleep(1)

    def lfrfid_em_create(self):
        keeb_hex = FlipperHEXKeyboard(self, "key")
        keeb_text = FlipperTextKeyboard(self, "key")
        self.main()
        self.send('loader open "125 kHz RFID"')
        sleep(2)
        self.key('SHORT DOWN')
        self.key('SHORT DOWN')
        self.key('SHORT OK')
        self.key('SHORT OK')
        keeb_hex.send("DC69660F12")
        sleep(0.1)
        keeb_text.send("Em")
        self.key('SHORT BACK')
        sleep(0.1)
        self.key('SHORT OK')
        sleep(0.1)
        self.key('SHORT OK')
        sleep(1)
        

    def lfrfid_hid_create(self):
        keeb_hex = FlipperHEXKeyboard(self, "key")
        keeb_text = FlipperTextKeyboard(self, "key")
        self.main()
        self.send('loader open "125 kHz RFID"')
        sleep(2)
        self.key('SHORT DOWN')
        self.key('SHORT DOWN')
        self.key('SHORT OK')
        self.key('SHORT DOWN')
        self.key('SHORT OK')
        keeb_hex.send("F4DBAC")
        sleep(0.1)
        keeb_text.send("Hid")
        self.key('SHORT BACK')
        sleep(0.1)
        self.key('SHORT OK')
        sleep(0.1)
        self.key('SHORT OK')
        sleep(1)
        
    def lfrfid_indala_create(self):
        keeb_hex = FlipperHEXKeyboard(self, "key")
        keeb_text = FlipperTextKeyboard(self, "key")
        self.main()
        self.send('loader open "125 kHz RFID"')
        sleep(2)
        self.key('SHORT DOWN')
        self.key('SHORT DOWN')
        self.key('SHORT OK')
        self.key('SHORT DOWN')
        self.key('SHORT DOWN')
        self.key('SHORT OK')
        keeb_hex.send("B82191")
        sleep(0.1)
        keeb_text.send("Ind")
        self.key('SHORT BACK')
        sleep(0.1)
        self.key('SHORT OK')
        sleep(0.1)
        self.key('SHORT OK')
