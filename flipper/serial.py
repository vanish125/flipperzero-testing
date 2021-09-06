import os
import serial
import time
import hashlib
import math


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
    CLI_PROMPT = ">: "
    CLI_EOL = "\r\n"

    def __init__(self, portname: str):
        self.port = serial.Serial()
        self.port.port = portname
        self.port.timeout = 2
        self.port.baudrate = 115200
        self.read = BufferedRead(self.port)
        self.last_error = ""

    def start(self):
        self.port.open()
        self.port.reset_input_buffer()
        # Send a command with a known syntax to make sure the buffer is flushed
        self.send("device_info\r")
        self.read.until("hardware_model      :")
        # And read buffer until we get prompt
        self.read.until(self.CLI_PROMPT)

    def stop(self):
        self.port.close()

    def send(self, line):
        self.port.write(line.encode("ascii"))

    def back(self, line):
        self.send("input_send back press\r")
        self.send("input_send back short\r")
        self.send("input_send back release\r")
        

    def send_and_wait_eol(self, line):
        self.send(line)
        return self.read.until(self.CLI_EOL)

    def send_and_wait_prompt(self, line):
        self.send(line)
        return self.read.until(self.CLI_PROMPT)

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

