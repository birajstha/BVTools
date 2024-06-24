from os import path, system
import takePic.take_pictures as tp
from art import *
from requests import get
from time import sleep
from sys import exit
from documentation.uitls import *
import colorama


def get_case():
    case = input("Enter Case / Loan Number: ")
    if (case == ""): 
        print("Make sure the case/loan number is valid..")
        get_case()
    case.upper()
    return case

def document(settings, logger):
    case_no = get_case()
    equipment_list = make_equipment_list()

    test_folder_path = settings['test_folder_path']

    try:
        make_folders(case_no, test_folder_path)
    except:
        message = "Folder creation failed"
        show_error(message)

    try:  
        for equipment in equipment_list[1:]:
            print(f"Take picture for {equipment[1]}")
            tp.take_pictures(equipment,test_folder_path, case_no, settings)
    except Exception as e:
        message = "Failed to initialize camera"
        show_error(e)

    total_time = 0
    for equipment in equipment_list[1:]:
        qtr_hr = test_equipment(equipment)
        equipment[2] = check_tested_good_bad(equipment[1])
        equipment[3] = input("Enter Remark : ")
        equipment[4] = qtr_hr
        total_time += qtr_hr
    #subprocess.call('C:\Vision\Recorder\Recorder.exe')
    #os.system("Recorder")
    tabulated_data = tabulate_data(equipment_list)
    write_to_txtsummary(tabulated_data, case_no, settings)

    report_loc = path.join(f"{test_folder_path}/{case_no}/InternalTestResults/TestSummary.txt")
    system(f"Notepad {report_loc}")
    copy_log_files(settings['recorder_log_path'], path.join(f"{test_folder_path}/{case_no}/InternalTestResults/LogFiles/"))
    bye("Good Day !!")
    logger.info(f"{case_no} testing completed")
    message = "Exiting now ..."
    sleep(3)
    return 0

def main(AppName, version, logger):
    welcome(f"{AppName}", version)
    if license['License'] != "BrainVision":
        print(license['Message'])
        sleep(3)
        print("Exiting now ..")
        sleep(2)
        raise Exception
    
    try:
        settings = get_setup()
    except Exception as e: 
        message = "Setup file not valid!"
        show_error(message)
    
    document(settings, logger)
    exit()

if __name__== "__main__":
    colorama.init()
    url = "https://raw.githubusercontent.com/birajstha/license/main/BVLicense.txt"
    resp = get(url)
    text = resp.text
    license = {}
    for line in text.split('\n'):
        if line:
            key, value = line.split(':')
            license[key] = value.strip()

    from logger import logger
    try:
        main(license['AppName'], license['Version'], logger)
    except Exception as e:
        logger.critical(license['Message'])
        print(e)
        exit()

  
