#!/usr/bin/env python3
# protoc -I=./flipperzero-protobuf --python_out=./flipper_proto_compiled ./flipperzero-protobuf/*.proto
# sed -i ./flipper_proto_compiled/*_pb2.py -e 's/^import [^ ]*_pb2/from . \0/'
# -*- coding: utf-8 -*-

from socket import timeout
import sys
from turtle import screensize
import serial
import time
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32

from flipper_proto_compiled import flipper_pb2, system_pb2, gui_pb2

import numpy

res_x = 128
res_y = 64
n = 0


def system_ping_cmd(id=0, data=bytes([0xde, 0xad, 0xba, 0xba, 0xca, 0xca])):
    flipper_message = flipper_pb2.Main()
    flipper_message.command_id = id
    flipper_message.command_status = flipper_pb2.CommandStatus.Value('OK')
    flipper_message.has_next = False
    ping = system_pb2.PingRequest()
    ping.data = data
    flipper_message.system_ping_request.CopyFrom(ping)
    # print(bytearray(_VarintBytes(flipper_message.ByteSize()) + flipper_message.SerializeToString()))
    return bytearray(_VarintBytes(flipper_message.ByteSize()) + flipper_message.SerializeToString())


def system_alert_cmd(id=0):
    flipper_message = flipper_pb2.Main()
    flipper_message.command_id = id
    flipper_message.command_status = flipper_pb2.CommandStatus.Value('OK')
    flipper_message.has_next = False
    alert = system_pb2.PlayAudiovisualAlertRequest()
    flipper_message.system_play_audiovisual_alert_request.CopyFrom(alert)
    return bytearray(_VarintBytes(flipper_message.ByteSize()) + flipper_message.SerializeToString())


def gui_stream_cmd(id=0):
    flipper_message = flipper_pb2.Main()
    flipper_message.command_id = id
    flipper_message.command_status = flipper_pb2.CommandStatus.Value('OK')
    flipper_message.has_next = False
    stream = gui_pb2.StartScreenStreamRequest()
    flipper_message.gui_start_screen_stream_request.CopyFrom(stream)
    return bytearray(_VarintBytes(flipper_message.ByteSize()) + flipper_message.SerializeToString())


def main():
    flipper = serial.Serial(sys.argv[1], timeout=1)
    flipper.baudrate = 230400
    # flipper.timeout = 1
    flipper.flushOutput()
    flipper.flushInput()
    flipper.write(b"\nstart_rpc_session\r")  # once

    # Read garbage
    flipper.read(size=1000)

    buffer = bytearray()
    i = 0
    try:
        # while True:
        # flipper.write(system_ping_cmd(i))
        i = 1
        # flipper.write(system_alert_cmd(i))
        flipper.flushOutput()
        flipper.flushInput()
        flipper.write(gui_stream_cmd(i))
        while True:
            if flipper.inWaiting():
                buffer += (flipper.read(flipper.inWaiting()))
            if len(buffer):
                print(buffer)
                n = 0
                while n < len(buffer):
                    msg_len, new_pos = _DecodeVarint32(buffer, n)
                    print(msg_len, new_pos)
                    n = new_pos
                    msg_buf = buffer[n:msg_len]
                    n = msg_len
                    # message = flipper_pb2.Main()
                    # message.ParseFromString(msg_buf)
                    # screen_frame = gui_pb2.ScreenFrame()
                    # screen_frame.CopyFrom(message.gui_screen_frame)
                    # print(screen_frame.data)
            # time.sleep(0.1)

        # rx = flipper.read(size=1030)
        # print(f'Rx: {rx}')
    finally:
        flipper.close()


"""

    while n == 0:
        ser.read_until(bytes.fromhex('F0E1D2C3'))
        data = ser.read(int(res_x*res_y/8))

        def get_bin(x): return format(x, 'b')

        scr = numpy.zeros((res_x+1, res_y+1))

    x = y = 0
    basey = 0

    for i in range(0, int(res_x*res_y/8)):
        tmp = get_bin(data[i])
        tmp = '0'*(8-len(tmp)) + tmp
        tmp = tmp[::-1]  # reverse

        y = basey
        x += 1
        for c in tmp:
            scr[x][y] = c
            y += 1

        if (i + 1) % res_x == 0:
            basey += 8
            x = 0

    print(chr(27) + "[2H")
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
    n = 1
"""

if __name__ == '__main__':
    main()
