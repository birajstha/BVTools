import os
import tabulate
import pandas as pd
import datetime
import shutil
import logging
logging.basicConfig(filename='FileTransfer.log', encoding='utf-8', level=logging.DEBUG)

dropzone = os.path.abspath("C:/Users/BShrestha/DropZone")
case = os.path.join(dropzone, "L_SupportData/Cases")

destination = os.path.join(dropzone,"L_SupportData/Archive - For Deletion/Cases")
mypath = os.path.join(destination, f"{datetime.date.today()}")

def makeFolder():
    if not os.path.isdir(mypath):
        os.makedirs(mypath)


def main():
    cur_dir = os.getcwd()
    makeFolder()
    cases2archive = pd.read_excel("Cases_to_archive.xlsx")
    list = cases2archive["Case ID"].values
    #list = ["Test"]
    print(list)
    for dir in list:
        source = f"{case}/{dir}"
        if os.path.isdir(source):
            try:
                shutil.move(source, mypath)
                logging.info(f'{dir} moved.')

            except:
                logging.error(f"{dir} not moved !")
                continue
        else: logging.error(f"{dir} doesn't exist !")

    
if __name__ == "__main__":
    main()