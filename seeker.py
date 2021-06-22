#!/usr/bin/python3
import serial, binascii

MOTOR_ON = [0x3E, 0x45, 0x01, 0x46, 0x0B, 0x0B]
MOTOR_OFF = [0x3E, 0x45, 0x01, 0x46, 0x0C, 0x0C]
RETURN_HEAD = [0x3E, 0x45, 0x01, 0x46, 0x12, 0x12]
CENTER_YAW = [0x3E, 0x45, 0x01, 0x46, 0x23, 0x23]
LOOK_DOWN = [0x3E, 0x45, 0x01, 0x46, 0x11, 0x11]

HEAD = [0xFF, 0x01, 0x0F, 0x10]
CONTROL_MODE = [0x00, 0x00, 0x05] # mode yaw angle ref frame 
ROLL = [0x00, 0x00, 0x00, 0x00] # speed + angle
PITCH = [0x00, 0x00, 0x00, 0x00]
YAW = [0x00, 0x00, 0x00, 0x08] # yaw 45º
CHECKSUM = [0x0D]
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
            self.ser.write(self.commands[command])
            
    def read_serial(self):
        if type(self.command) == list:
            return binascii.hexlify(self.ser.readlines()[0]).decode('utf-8')
        else:
            return binascii.hexlify(self.ser.read()).decode('utf-8')