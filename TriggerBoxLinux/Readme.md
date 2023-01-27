## Introduction
Brain Products provides drivers for [TriggerBox](https://www.brainproducts.com/solutions/triggerbox/) only to be used with computers running Windows OS. TriggerBox uses chip FT2232H hence we can use PyFtdi library in python as a workaround solution to make it work with linux.

The example script `TriggerBox.py` uses pyFtdi library and shows how to configure custom VID/PID and add TriggerBox as a known device. Furthermore, the script sends triggers/markers from 1 to 255. The original script from Dr. Traunmüller, to mirror the input triggers to output, has been commented. You can un-comment and use those if required. 

## Prequisites
The library PyFtdi has prerequisites hence please follow the setup from [here](https://eblot.github.io/pyftdi/installation.html#prerequisites)

Please Note that all of the below commands implemented in the TriggerBox.py file. You just have to copy and modify the address that shows up when listing your device.

## Running the code 
`>> python3 TriggerBox.py`

![Screenshot](https://user-images.githubusercontent.com/111654544/215162350-fde38ff5-4f66-4337-8f34-136427451810.png)




## Thanks to
- Peter Traunmüller
- David Schubring
- Edward Lau

## More Reads - Sending markers to Brain Products amplifier systems
[Communication with the trigger port: A beginner’s guide](https://pressrelease.brainproducts.com/trigger-beginners-guide/)
