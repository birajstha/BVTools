# BVTools

# Introduction
This project is aimed to add tools to help work with Brain Product's amplifier and systems.
This project uses following libraries so please install them first using command :
`pip install -r requirements.txt`

- colorama==0.4.6
- pyftdi==0.54.0
- pyparallel==0.2.2
- pyserial==3.5
- pyusb==1.2.1
- simple-term-menu==1.5.2

This repo consists of few tools 
## 1. [PlotChargeCycle](https://github.com/birajstha/BVTools/tree/main/PlotChargeCycle) (Windows/Mac/Linux)
- This python application will take in a log file spit out by your Brain Product's amplifier to plot the battery charge cycle.
- This has been helpful for determining if the battery is slowly losing its capacity, dying and if you will need a new battery.

## 2. [ASA](https://github.com/birajstha/BVTools/tree/main/AcousticStimulationAdapter%20(ASA)) 
- This contains python files to generate beep sound to test the Acoustic Stimulation Adapter / Stimtrak
- BeepSound.py > uses winsound which is only available for windows
- Sound.ipynb uses pyaudio. Please follow installation instructions [here](https://git.skeh.site/skeh/pyaudio)

## 3. [FileSize.py](https://github.com/birajstha/BVTools/blob/main/FileSize.py) (Windows/Mac/Linux)
- This python code calculates the approximate filesize of the recording by Brain Product's amplifiers.

## 4. [SerialPort_Write_TriggerBox.py](https://github.com/birajstha/BVTools/blob/main/SerialPort_Write_TriggerBox.py) (Windows Only)
- This python code is modified version of Brain Product's.
- It requires TriggerBox Test IO program to be installed on the Windows OS.
- Send markers via Virtual COM port -> TriggerBox -> Amplifier

## 5. [parallelPort](https://github.com/birajstha/BVTools/tree/main/parallelPort) (Linux)
- This python program is for Linux
- Refer to ReadMe.txt for setup of the Parallel port.

## 6. [LinuxTriggerBox.py](https://github.com/birajstha/BVTools/tree/main/TriggerBoxLinux) (Linux)
- This code is for using Brain Product's TriggerBox in Linux with python.
- It uses PyFtdi library in order write to FT2232H
- This code is modified version of Dr. Traumuller's.
