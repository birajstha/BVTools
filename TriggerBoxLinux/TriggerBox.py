#testscript for the brainproducts triggerbox
#writes the ft2232h via pyftdi
#Modified Biraj Shrestha 11.2022

from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioAsyncController
import time

#add the brainproducts Triggerbox to the known devices
Ftdi.add_custom_vendor(0x1103, "Brainproducts")
Ftdi.add_custom_product(0x1103, 0x0021)

#define the two GPIO ports (0-7 and 8-15)
gpio1 = GpioAsyncController()
gpio2 = GpioAsyncController()

#search for devices and print them
print("Found devices:")
Ftdi.show_devices()

#0 is in, 1 is out
gpio1.configure('ftdi://Brainproducts:0x0021:TB6QHXBF/1 ', direction=0b11111111) #1-8, all outputs
gpio2.configure('ftdi://Brainproducts:0x0021:TB6QHXBF/2 ', direction=0b00000000) #8-15, all inputs

gpio1.write(0x00) # set all outputs to zero
reset = 0
print("Testing all Triggers GPIO:")
for i in range (0, 255):
        print (f"Sending Trigger: {i}")
        gpio1.write(i)
        time.sleep(0.5)
        gpio1.write(reset)
        
#close
gpio1.close()
gpio2.close()

