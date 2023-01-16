## Introduction
Brain Products provides drivers for [TriggerBox](https://www.brainproducts.com/solutions/triggerbox/) only to be used with computers running Windows OS. TriggerBox uses chip FT2232H hence we can use PyFtdi library in python as a workaround solution to make it work with linux.

The example script `TriggerBox.py` uses pyFtdi library and shows how to configure custom VID/PID and add TriggerBox as a known device. Furthermore, the script sends triggers/markers from 1 to 255. The original script from Dr. Traunmüller, to mirror the input triggers to output, has been commented. You can un-comment and use those if required. 

## Prequisites
The library PyFtdi has prerequisites hence please follow the setup from [here](https://eblot.github.io/pyftdi/installation.html#prerequisites)

Please Note that all of the below commands implemented in the TriggerBox.py file. You just have to copy and modify the address that shows up when listing your device.
## Importing libraries

`>> from pyftdi.ftdi import Ftdi`

`>> from pyftdi.gpio import GpioAsyncController`

## Adding Brain Products TriggerBox as known devices
Please use Product ID (PID) = "0021" and Vendor ID (VID) = "1103"

`>> Ftdi.add_custom_vendor(0x1103, "Brainproducts")`

`>> Ftdi.add_custom_product(0x1103, 0x0021)`

## list your devices
- Please connect your TriggerBox and run `TriggerBox.py`

![UbuntuTB](https://user-images.githubusercontent.com/111654544/212751366-6ff4fcf8-8487-4c62-86c2-ebe0112aa4a8.png)*Source: David Schubring ( Technical Support/Brain Products)*

## Configuring TriggerBox

`gpio1.configure('ftdi://Brainproducts:0x0021:TB6QHXBF/1 ', direction=0b11111111) #1-8, all outputs`

`gpio2.configure('ftdi://Brainproducts:0x0021:TB6QHXBF/2 ', direction=0b00000000) #8-15, all inputs`

## Sending Markers
Import time module to sustain the outputs for required interval.

`>> import time` ==> used for sleep / pulse length

`>> gpio1.write(0x00)` ==> set all outputs to zero

`>> time.sleep(0.5)` ==> sleep for trigger pulse length, at least >2 sample points depending on sampling rate

`>> gpio1.write(0x05)` ==> send example trigger 5, please note that different number formats exist, e.g. 0x is hex, 0b is binary, etc. 

`>> time.sleep(0.5)` ==> sleep for trigger pulse length, at least >2 sample points depending on sampling rate

`>> gpio1.write(0x00)` ==> set all outputs to zero

## Closing the Ports

`gpio1.close()`

`gpio2.close()`

## Thanks to
- Peter Traunmüller
- David Schubring
- Edward Lau

## More Reads - Sending markers to Brain Products amplifier systems
[Communication with the trigger port: A beginner’s guide](https://pressrelease.brainproducts.com/trigger-beginners-guide/)