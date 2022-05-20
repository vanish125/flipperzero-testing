import os
import time
import hashlib
import math
import numpy

import serial

from PIL import Image
from PIL import ImageChops
from flipperzero_protobuf_py.flipper_protobuf import ProtoFlipper

def timing(func):
    """
    Speedometer decorator
    """

    def wrapper(*args, **kwargs):
        time1 = time.monotonic()
        ret = func(*args, **kwargs)
        time2 = time.monotonic()
        print(
            "{:s} function took {:.3f} ms".format(
                func.__name__, (time2 - time1) * 1000.0
            )
        )
        return ret

    return wrapper

class InputTypeException(Exception):
    pass

class BufferedRead:
    def __init__(self, stream):
        self.buffer = bytearray()
        self.stream = stream

    def until(self, eol="\n", cut_eol=True):
        eol = eol.encode("ascii")
        while True:
            # search in buffer
            i = self.buffer.find(eol)
            if i >= 0:
                if cut_eol:
                    read = self.buffer[:i]
                else:
                    read = self.buffer[: i + len(eol)]
                self.buffer = self.buffer[i + len(eol) :]
                return read

            # read and append to buffer
            i = max(1, self.stream.in_waiting)
            data = self.stream.read(i)
            self.buffer.extend(data)


class ImageCompare:
    def compare(self, name):
        image_path = "out"
        orig_path = "orig"
        image_one = Image.open(f'{image_path}/{name}').convert('RGB')
        image_two = Image.open(f'{orig_path}/{name}').convert('RGB')
        diff = ImageChops.difference(image_one, image_two).getbbox()
        if diff==None:
            print("Ok")
        else:
            print("Error")


class FlipperSerial:
    CLI_CTRL = "Press Ctrl+C to abort"
    CLI_PROMPT = ">: "
    CLI_EOL = '\r\n'

    def __init__(self, portname: str):
        self.port = serial.Serial()
        self.port.port = portname
        self.port.timeout = 2
        self.port.baudrate = 230400
        self.read = BufferedRead(self.port)
        self.last_error = ""

    def start(self):
        self.port.open()
        self.port.reset_input_buffer()
        # Send a command with a known syntax to make sure the buffer is flushed
        self.send("device_info")
        self.read.until("hardware_model")
        # And read buffer until we get prompt
        self.read.until(self.CLI_PROMPT)

    def stop(self):
        self.port.close()

    def send(self, line):
        self.port.flushOutput()
        self.port.flushInput()
        self.port.write(line.encode("ascii") + "\r".encode("ascii"))
        time.sleep(0.1)

    def send_and_wait_eol(self, line):
        self.send(line)
        return self.read.until(self.CLI_EOL).decode("ascii")

    def send_and_wait_prompt(self, line):
        self.send(line)
        data = self.read.until(self.CLI_PROMPT).decode("ascii")
        data = data[len(line)+1:]
        return data

    def send_and_wait_ctrl(self, line):
        self.send(line)
        data = self.read.until(self.CLI_CTRL).decode("ascii")
        return data

    def read_until_promp(self):
        return self.read.until(self.CLI_PROMPT).decode("ascii")

    def has_error(self, data):
        """Is data has error"""
        if data.find(b"Storage error") != -1:
            return True
        else:
            return False

    def get_error(self, data):
        """Extract error text from data and print it"""
        error, error_text = data.decode("ascii").split(": ")
        return error_text.strip()

    def main(self):
        for i in range(7): 
            self.key("SHORT BACK")

    def CTRLc(self):
        self.port.write(b'\x03')
        time.sleep(0.1)

    def RPC_start(self):
        return self.send_and_wait_eol("start_rpc_session")

    def RPC_stop(self):
        proto = ProtoFlipper(self.port)
        proto.cmd_flipper_stop_session()
        time.sleep(0.1)

    def RPC_key(self, key):
        proto = ProtoFlipper(self.port)
        proto.cmd_gui_send_input(key)
        time.sleep(0.1)

    def key(self, key):
        type, key = key.split(" ")

        if type != 'SHORT' and type != 'LONG':
            raise InputTypeException('Incorrect type')

        if key != 'UP' and key != 'DOWN' and key != 'LEFT' and key != 'RIGHT' and key != 'OK' and key != 'BACK':
            raise InputTypeException('Incorrect key')

        self.send('input send '+ key.lower()+ ' press')
        print('input send '+ key.lower()+ ' press')
        self.send('input send '+ key.lower()+ ' '+ type.lower())
        print('input send '+ key.lower()+ ' '+ type.lower())
        self.send('input send '+ key.lower()+ ' release')
        print('input send '+ key.lower()+ ' release')

    def imageFile(self, name):
        image_path = "out"
        res_x = 128
        res_y = 64
        self.RPC_start()
        proto = ProtoFlipper(self.port)
        data = proto.cmd_gui_snapshot_screen()
        get_bin = lambda x: format(x, 'b')
        scr = numpy.zeros((res_x+1, res_y+1))
        x = y = 0
        basey = 0
        for i in range(0, int(res_x*res_y/8)):
            tmp = get_bin(data[i])
            tmp = '0'*(8-len(tmp)) + tmp
            tmp = tmp[::-1]     #reverse        
            y = basey
            x += 1
            for c in tmp:
                scr[x][y] = c
                y += 1   
            if (i + 1) % res_x == 0:
                basey += 8
                x = 0
        #export to image file:
        scale = 3
        col_black = [0x11, 0x11, 0x11]
        col_white = [0xff, 0x8c, 0x29]
        col_bg = col_black
        img = numpy.zeros((res_y*scale, res_x*scale, 3), dtype=numpy.uint8)
        for y in range(0, res_y*scale):
            for x in range(0, res_x*scale):
                img[y][x] = col_bg
        for y in range(0, res_y):
            for x in range(1, res_x+1):
                if int(scr[x][y]) == 1:
                    for yy in range(y*scale, (y+1)*scale):
                        for xx in range((x-1)*scale, x*scale):
                            img[yy][xx] = col_black
                else:
                    for yy in range(y*scale, (y+1)*scale):
                        for xx in range((x-1)*scale, x*scale):
                            img[yy][xx] = col_white
                            #img[y*scale][(x-1)*scale] = col_white

        im = Image.new('RGB', (res_x, res_y))
        im = Image.fromarray(img)
        im.save(f'{image_path}/{name}')
        print('Saved to', name)
        self.RPC_stop()