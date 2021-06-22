#!/usr/bin/python3
import serial, binascii

MOTOR_ON = ('\x3E\x45\x01\x46\x0B\x0B')
MOTOR_OFF = ('\x3E\x45\x01\x46\x0C\x0C')
RETURN_HEAD = ('\x3E\x45\x01\x46\x12\x12')
CENTER_YAW = ('\x3E\x45\x01\x46\x23\x23')
LOOK_DOWN = ('\x3E\x45\x01\x46\x11\x11')

HEAD = ('\xFF\x01\x0F\x10')
CONTROL_MODE = ('\x00\x00\x05') # mode yaw angle ref frame 
ROLL = ('\x00\x00\x00\x00') # speed + angle
PITCH = ('\x00\x00\x00\x00')
YAW = ('\x00\x00\x00\x08') # yaw 45º
CHECKSUM = ('\x0D')
YAW_45 = HEAD + CONTROL_MODE + ROLL + PITCH + YAW + CHECKSUM # FF 01 0F 10 00 00 05 00 00 00 00 00 00 00 00 00 00 00 08 0D

class Seeker():

    def __init__(self):
        self.commands = {'motor-on': MOTOR_ON, 'motor-off': MOTOR_OFF, 
        'return-head': RETURN_HEAD, 'center-yaw': CENTER_YAW, 'look-down': LOOK_DOWN, 
        'yaw-45': YAW_45}
        self.ser = ''

    def open_serial(self, device_path='/dev/ttyUSB0', baudrate=115200):
        self.ser = serial.Serial(device_path, baudrate, timeout=1)

    def close_serial(self):
        self.ser.close()

    def send_command(self, command):
        self.command = command
        if type(command) == str:
            self.ser.write(str.encode(self.commands[command]))
            print(str.encode(self.commands[command]))
            
    def read_serial(self):
        if type(self.command) == list:
            return binascii.hexlify(self.ser.readlines()[0]).decode('utf-8')
        else:
            return binascii.hexlify(self.ser.read()).decode('utf-8')