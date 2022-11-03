# BVTools

This project is aimed to add tools to help work with Brain Product's amplifier and systems.

This repo consists of few tools 
1. PlotChargeCycle (Windows/Mac/Linux)
- This python application will take in a log file spit out by your Brain Product's amplifier to plot the battery charge cycle.
- This has been helpful for determining if the battery is slowly losing its capacity, dying and if you will need a new battery.

2. BeepSound.py (Windows/Mac/Linux)
- This python code generates beep sound to test the Acoustic Stimulation Adapter / Stimtrak

3. FileSize.py (Windows/Mac/Linux)
- This python code calculates the approximate filesize of the recording by Brain Product's amplifiers.

4. SerialPort_Write_TriggerBox.py (Windows Only)
- This python code is modified version of Brain Product's code. 
- It requires TriggerBox Test IO program to be installed on the Windows OS.
- Send markers via Virtual COM port -> TriggerBox -> Amplifier

5. parallelPort (Linux)
- This python program is for Linux
- Refer to ReadMe.txt for setup of the Parallel port.

6. BirajLinuxTriggerBox.py (Linux)
- This code is for using Brain Product's TriggerBox in Linux with python.
- It uses PyFtdi library in order write to FT2232H
- This code is modified version of Dr. Traumuller code.
