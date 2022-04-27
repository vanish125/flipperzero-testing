import os
import time
import hashlib
import math
import serial


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
            self.send("input send back press")
            self.send("input send back short")
            self.send("input send back release")

    def CTRLc(self):
        self.port.write(b'\x03')
        time.sleep(0.1)

    def RPS_stop(self):
        self.port.write(b'\x03\x9a\x01\x00')
        time.sleep(0.1)

    def up(self):
        self.send("input send up press")
        self.send("input send up short")
        self.send("input send up release")
    
    def down(self):
        self.send("input send down press")
        self.send("input send down short")
        self.send("input send down release")

    def left(self):
        self.send("input send left press")
        self.send("input send left short")
        self.send("input send left release")

    def right(self):
        self.send("input send right press")
        self.send("input send right short")
        self.send("input send right release")

    def ok(self):
        self.send("input send ok press")
        self.send("input send ok short")
        self.send("input send ok release")

    def back(self):
        self.send("input send back press")
        self.send("input send back short")
        self.send("input send back release")

    def lup(self):
        self.send("input send up press")
        self.send("input send up long")
        self.send("input send up release")
    
    def ldown(self):
        self.send("input send down press")
        self.send("input send down long")
        self.send("input send down release")

    def lleft(self):
        self.send("input send left press")
        self.send("input send left long")
        self.send("input send left release")

    def lright(self):
        self.send("input send right press")
        self.send("input send right long")
        self.send("input send right release")

    def lk(self):
        self.send("input send ok press")
        self.send("input send ok long")
        self.send("input send ok release")

    def lback(self):
        self.send("input send back press")
        self.send("input send back long")
        self.send("input send back release")


