# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 12:47:30 2022

@author: BShrestha
"""

import winsound
import time

frequency = 2000  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
count = 10

for i in range(0,count):
    winsound.Beep(frequency, duration)
    time.sleep(0.5)

