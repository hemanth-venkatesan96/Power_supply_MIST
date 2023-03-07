#!/bin/bash 
from serial import Serial
import serial.tools.list_ports

import time

def vset(v):
    return b"VSET1:" + bytes(str(v), encoding="ascii") + b'\n'

if __name__ == "__main__":
    print("Detected serial ports: ")

    for p in serial.tools.list_ports.comports():
        print("  " + p.device + " - " + p.description)

    print()

    port = input("Type in port name for GPD 4303s: ")
    
    print()
    ser = Serial(port, baudrate=9600)

    print("Attempting to identify GPD-4303S at serial port " + port + "...")
    ser.write(b"*IDN?\r")
    print()
    print("Reply: " + ser.readline().decode())
    print()

    vstart = float(input("Start voltage [V]: "))
    vend   = float(input("End voltage   [V]: "))
    vstep  = float(input("Step voltage  [V]: "))

    ser.write(b"OUT1\n")

    v = vstart
    while v <= vend:
        print("Setting output voltage to " + str(v) + " V")
        ser.write(vset(v))
        time.sleep(5)
        v += vstep