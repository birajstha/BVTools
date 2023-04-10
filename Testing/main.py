import os
from datetime import datetime
import take_pictures as tp
from art import *
from colorama import Fore, Style
import tabulate
import math


def write_to_txtsummary(to_write, case_no):
    path = os.path.join(f"{case_no}/InternalTestResults")
    f = open(f"{path}/TestSummary.txt", "w")
    f.write("="*26 + f"\nRelated Entity : {case_no} \n" +"="*26 +\
        f"\nTested on : {datetime.today().strftime('%Y-%m-%d')}\n" +\
        f"Tested by : Biraj Shrestha")
    f.write("\n\nTest Summary\n")
    f.write (to_write)


   
def welcome(text):
    Art = text2art(text)
    print(Art)
    print(Fore.RED +"#"*75)
    print(Fore.GREEN + "Welcome to Biraj's Test Documentation Application. \nPlease Enter the the following information below ! \nPress 'q' Enter to stop or ctrl + c to break!")
    print(Fore.RED +"#"*75)
    print(Style.RESET_ALL)

def make_folders(case_no):
    os.makedirs(f"{case_no}")
    os.makedirs(f"{case_no}/InternalTestResults")
    os.makedirs(f"{case_no}/InternalTestResults/RawData")
    os.makedirs(f"{case_no}/InternalTestResults/Pictures")
    os.makedirs(f"{case_no}/InternalTestResults/LogFiles")

def tabulate_data(data):    
    results = tabulate.tabulate(data[1:], headers=data[0], tablefmt="outline")
    return results

def make_equipment_list():
    equipment_list = []
    equipment_list.append(["Equipment Name", "Serial Number", "Tested Good/Bad", "Remarks", "Time (QTR HR)"])
    count = 1
    while (True):
        to_do = menu(count)
        count = count + 1
        if (to_do == "q"): break
        equipment_list.append([input("Name: "), input("SN: "), "NA", "NA", "1"])
    return equipment_list

def menu(count):
    return input(f"= Equipment_{count} = ")


def test_equipment(equipment):
    # Testing here
    # Screen saver caffeine and count timer
    start_time = datetime.now()
    print(Fore.RED +"#"*75)
    print(Fore.GREEN + f"Go ahead and Test the {equipment[0], equipment[1]}. \nTimer is started at {start_time}.\nWhen done enter 123 to continue..")
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
    qtr_hr = math.ceil(qtr_hr)
    if qtr_hr < 1: return 1
    return qtr_hr

def bye(text):
    Art = text2art(text)
    print(Fore.RED +"#"*75)
    print(Fore.GREEN + f"{Art}")
    print(Fore.RED +"#"*75)
    print(Style.RESET_ALL)

def main():
    welcome("Biraj-Tools")
    case_no = input("Enter Case / Loan Number: ")
    equipment_list = make_equipment_list()
    make_folders(case_no)
    for equipment in equipment_list[1:]:
        print(f"Take picture for {equipment[1]}")
        tp.take_pictures(equipment, case_no)

    total_time = 0
    for equipment in equipment_list[1:]:
        qtr_hr = test_equipment(equipment)
        test_input = input(f"How did this {equipment[1]} test? (1 = Good / 0 = Bad) : ")
        if (test_input == "1"): 
            equipment[2] = "GOOD"
            equipment[3] = input("Enter Remark : ")
        elif (test_input == "0"): 
            equipment[2] = "BAD"
            equipment[3] = input("Enter Remark : ")
        else: print("invalid ! Enter manually later")
        equipment[4] = qtr_hr
        total_time += qtr_hr
    #subprocess.call('C:\Vision\Recorder\Recorder.exe')
    #os.system("Recorder")
    tabulated_data = tabulate_data(equipment_list)
    write_to_txtsummary(tabulated_data, case_no)

    report_loc = os.path.join(f"{case_no}/InternalTestResults/TestSummary.txt")
    os.system(f"Notepad {report_loc}")
    bye("Good Day !!")


if __name__== "__main__":
    main()
    
  



