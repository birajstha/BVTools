#testscript for the brainproducts triggerbox
#writes the ft2232h via pyftdi
#original by peter traunmüller 3.2021
#modified by david schubring 1.2023
#Modified by Biraj Shrestha 11.2022, 01.23

from pyftdi.ftdi import Ftdi
from pyftdi.gpio import GpioAsyncController
import time
import sys
from io import StringIO
from contextlib import redirect_stdout
catcher = StringIO()


#add the brainproducts Triggerbox to the known devices
Ftdi.add_custom_vendor(0x1103, "Brainproducts")
Ftdi.add_custom_product(0x1103, 0x0021)

#define the two GPIO ports (0-7 and 8-15)
gpio1 = GpioAsyncController()
gpio2 = GpioAsyncController()
        
try :
        with redirect_stdout(catcher):
                exec('Ftdi.show_devices()')
        devices = catcher.getvalue()
        TB = devices.split()

        #0 is in, 1 is out
        # Copy the address shown in the found devices above
        gpio1.configure(f'{TB[2]}', direction=0b11111111) #1-8, all outputs
        gpio2.configure(f'{TB[4]}', direction=0b00000000) #8-15, all inputs

        gpio1.write(0x00) # set all outputs to zero
        reset = 0
        print("Testing all Triggers GPIO:")
        for i in range (0, 255):
                print (f"Sending Trigger: {i}")
                gpio1.write(i)
                time.sleep(0.5)
                gpio1.write(reset)
                
        ### Original example that mirrors trigger input ###

        #print("Read GPIO:")
        #last_gpio2 = 0
        #while True:
        #        this_gpio2 = gpio2.read() #read inputs 8-15
        #        if last_gpio2 != this_gpio2: #check if they have changed
        #                print("2:" + str(bin(this_gpio2))) #print inputs as binary 
        #                gpio1.write(this_gpio2) #set the outputs to the just read input values
        #        last_gpio2 = this_gpio2 


        #close
        gpio1.close()
        gpio2.close()

except:
        print("Please connect TriggerBox and Try Again!")