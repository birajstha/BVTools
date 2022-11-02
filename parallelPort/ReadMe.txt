parallelPortTest.py sends out triggers from 1-255 with interval of 100ms.
This code is helpful to test and build upon python application to send Event markers to BrainVision Amplifiers.

Step 1
$ pip install pyparallel
more information at https://pypi.org/project/pyparallel/

Step 2
Make sure there is parporto inside /dev
$ ls /dev | grep parport0
or 
$ cat /proc/ioports

Step 3
Set access to the parallel port
$ sudo chmod 666 /dev/parport0

Step 4
(Ubuntu)If you run into problem: Device not found run
$ sudo modprobe -r lp

Step 5
Run parallelport.py
