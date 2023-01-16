## Introduction
Brain Products provides drivers for TriggerBox only to be used with computers running Windows OS. TriggerBox uses chip FT2232H hence we can use PyFtdi library in python as a workaround solution to make it work with linux.

## Prequisites
The library PyFtdi has prerequisites hence please follow the setup from [here](https://eblot.github.io/pyftdi/installation.html#prerequisites)

## list your devices
- Please connect your TriggerBox and run following command in python. 

`>> from pyftdi.ftdi import Ftdi`

`>> Ftdi.show_devices()`

- You should see your TriggerBox listed as follows

`ftdi://Brainproducts:0x0021:TB6QHXBF/1  (TriggerBox)`

`ftdi://Brainproducts:0x0021:TB6QHXBF/2  (TriggerBox)`

- Now, copy the above address `TB6QHXBF/1` , `TB6QHXBF/2`  to use in 
`gpio1.configure()` function in LinuxTriggerBox.py

![UbuntuTB](https://user-images.githubusercontent.com/111654544/212751366-6ff4fcf8-8487-4c62-86c2-ebe0112aa4a8.png)*Source: David S Brain Products*
