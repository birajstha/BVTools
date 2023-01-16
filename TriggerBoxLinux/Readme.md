## Introduction
Brain Products provides drivers for TriggerBox only to be used with computers running Windows OS. TriggerBox uses chip FT2232H hence we can use PyFtdi library in python as a workaround solution to make it work with linux.
The example script `TriggerBox.py` shows how to use custom VID/PID to add TriggerBox as a known device. Furthermore, the script sends triggers/markers from 1 to 255. The original script from Dr. Traunmüller, to mirror the input triggers to output, has been commented. You can un-comment and use those if required. 

## Prequisites
The library PyFtdi has prerequisites hence please follow the setup from [here](https://eblot.github.io/pyftdi/installation.html#prerequisites)

Please Note that all of the below commands implemented in the TriggerBox.py file. You just have to copy and modify the address that shows up when listing your device.
## Importing libraries

`>> from pyftdi.ftdi import ftdi`

`>> from pyftdi.gpio import GpioAsyncController`

## Adding Brain Products TriggerBox as known devices
Please use Product ID (PID) = "0021" and Vendor ID (VID) = "1103"

`>> ftdi.add_custom_vendor(0x1103, "Brainproducts")`

`>> ftdi.add_custom_product(0x1103, 0x0021)`

## list your devices
- Please connect your TriggerBox and run `TriggerBox.py`

![UbuntuTB](https://user-images.githubusercontent.com/111654544/212751366-6ff4fcf8-8487-4c62-86c2-ebe0112aa4a8.png)*Source: David Schubring ( Technical Support/Brain Products)*

## Configuring TriggerBox

`gpio1.configure('ftdi://Brainproducts:0x0021:TB6QHXBF/1 ', direction=0b11111111) #1-8, all outputs`

`gpio2.configure('ftdi://Brainproducts:0x0021:TB6QHXBF/2 ', direction=0b00000000) #8-15, all inputs`

## Sending Markers

`>> gpio1.write(0x01)`

## Close the Ports

`gpio1.close()`

`gpio2.close()`