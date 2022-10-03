# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:42:26 2022

@author: BShrestha
"""

import serial
import time

PulseWidth = 1

# Open the Windows device manager, search for the "TriggerBox VirtualSerial Port (COM6)"
# in "Ports /COM & LPT)" and enter the COM port number in the constructor.
port = serial.Serial("COM3")

# Set the port to an initial state
port.write([0x00])
time.sleep(PulseWidth)

# Set Bit 0, Pin 2 of the Output(to Amp) connector
port.write([0x0F])
time.sleep(PulseWidth)

# Reset Bit 0, Pin 2 of the Output(to Amp) connector
port.write([0x00])
time.sleep(PulseWidth)

# Reset the port to its default state
port.write([0xFF])
time.sleep(PulseWidth)


# Close the serial port
port.close()