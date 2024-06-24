from os import path, makedirs, system
from datetime import datetime
from art import *
from colorama import Fore, Style
import tabulate
from math import ceil
from time import sleep
from sys import exit
from shutil import copytree
from logger import logger


def write_to_txtsummary(to_write, case_no, settings):
    path_to_write = path.join(f"{case_no}/InternalTestResults")
    try:
        with open(f"{path_to_write}/TestSummary.txt", "w") as f:
            f.write("="*26 + f"\nRelated Entity : {case_no} \n" +"="*26 +\
                f"\nTested on : {datetime.today().strftime('%Y-%m-%d')}\n")
            
            f.write(f"Tested by : {settings['tested_by']}")
            f.write("\n\nTest Summary\n")
            f.write(to_write)
            f.write("\n\n")
    except: 
        message = 'Summary creation failed'
        show_error(message)

def show_error(message):
    logger.error(message)
    print(message)
    sleep(3)
    exit()
  
def welcome(text, version):
    Art = text2art(text)
    print(Art)
    print(Fore.RED +"#"*75)
    print(Fore.GREEN + f"""
    Welcome to Test Documentation Application V {version}.
    Copyright \u00A9 2023, Biraj Shrestha.
    Press 'q' then Enter to stop or ctrl + c to break!
    Press Enter to add next equipment. Do not use '/' or '\\' in the input
    """)
    print(Fore.RED +"#"*75)
    print(Style.RESET_ALL)

def make_folders(case_no, test_folder_path):
    makedirs(f"{test_folder_path}/{case_no}")
    makedirs(f"{test_folder_path}/{case_no}/InternalTestResults")
    makedirs(f"{test_folder_path}/{case_no}/InternalTestResults/RawData")
    makedirs(f"{test_folder_path}/{case_no}/InternalTestResults/Pictures")
    #makedirs(f"{test_folder_path}/{case_no}/InternalTestResults/LogFiles")

def tabulate_data(data):    
    results = tabulate.tabulate(data[1:], headers=data[0], tablefmt="outline")
    return results

def make_equipment_list():
    equipment_list = []
    equipment_list.append(["Equipment Name", "Serial Number", "Tested Good/Bad", "Remarks", "Time (QTR HR)"])
    count = 1
    while (True):
        to_do = menu(count)
        if (to_do.lower() == "q"): break
        elif (to_do == ""): 
            equipment_name = input("Name : ")
            equipment_sn = input("SN : ")
            equipment_list.append([equipment_name, equipment_sn, "NA", "NA", "1"])
        else: continue
        count = count + 1
    return equipment_list

def menu(count):
    return input(f"= Equipment_{count} = ")


def test_equipment(equipment):
    # Testing here
    # Screen saver caffeine and count timer
    start_time = datetime.now()
    print(Fore.RED +"#"*75)
    print(Fore.GREEN + f"Testing {equipment[0]} SN: {equipment[1]}. \nTimer is started at {start_time}.\nWhen done enter 123 to continue...")
    print(Fore.RED +"#"*75)
    print(Style.RESET_ALL)
    while (True):
        key_press = input("Done yet? : ")
        if (key_press == "123"): 
            stop_time = datetime.now()
            break
    
    print(f"Stopped at : {stop_time}")
    elapsed_time = stop_time - start_time
    print(f"Elapsed Time : {elapsed_time}")
    qtr_hr = round((elapsed_time.seconds)/(15*60),2)
    print(f"It took {qtr_hr} number of quarter hours")
    print(Fore.RED +"#"*75)
    print(Style.RESET_ALL)
    qtr_hr = ceil(qtr_hr)
    if qtr_hr < 1: return 1
    return qtr_hr

def bye(text):
    Art = text2art(text)
    print(Fore.RED +"#"*75)
    print(Fore.GREEN + f"{Art}")
    print(Fore.RED +"#"*75)
    print(Style.RESET_ALL)

def get_setup():
    setup_data = {}
    with open('settings.txt', 'r') as text:
        for line in text.readlines():
            if line:
                key, value = line.split(':')
                setup_data[key] = value.strip()
    return setup_data

def check_tested_good_bad(equipment):
    test_input = input(f"How did this {equipment} test? (1 = Good / 0 = Bad) : ")
    if (test_input == "1"): 
            return "GOOD"
    elif (test_input == "0"): 
            return "BAD"
    else: 
        print("Invalid input!!! Please enter 0 or 1 ")
        return check_tested_good_bad(equipment)
    
def copy_log_files(src_dir, dst_dir):
    copytree(src_dir, dst_dir)