## Introduction
Brain Products TriggerBox uses chip FT2232H hence we can use PyFtdi library to access via python.

## Prequisites
The library PyFtdi has prerequisites hence please follow the setup from [here](https://eblot.github.io/pyftdi/installation.html#prerequisites)

To list your devices:
`from pyftdi.ftdi import Ftdi`
`Ftdi.show_devices()`

If you could see your devices listed as
`Brainproducts:0x0021:TB6QHXBF/1 `
`Brainproducts:0x0021:TB6QHXBF/2 `
then, you can copy the address to use in 
`gpio1.configure()` function in LinuxTriggerBox.py
