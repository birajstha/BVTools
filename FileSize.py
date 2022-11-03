"""
@Author: Biraj Shrestha

"""
from simple_term_menu import TerminalMenu
from colorama import Fore, Style 

def FileSizeCalculator(amplifier, samplingRate, channelNumber, recordingTime):
	adc = 24;
	if amplifier.upper() == "BRAINAMP":
		adc = 16;

	return (adc *samplingRate * channelNumber * recordingTime*60 /8 /1024 /1024)

if (__name__) == "__main__":
	amp_list = ['BrainAmp', 'actiCHamp', 'LiveAmp']
	print("Select Amplifier: ")
	menu = TerminalMenu(amp_list)
	amplifier = amp_list[menu.show()]
	print(amplifier)
	samplingRate = int(input("samplingRate (Hz): "))
	channelNumber = int(input("channelNumber: "))
	recordingTime  = float(input("recordingTime (mins): "))
	fileSize = FileSizeCalculator(amplifier, samplingRate, channelNumber, recordingTime);
	print (Fore.GREEN + f"The Approximate size of recording is : {round(fileSize, 2)} MB")
	if amplifier == "LiveAmp": print(Fore.RED + "Onboard recording would be even less")
