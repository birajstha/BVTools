def FileSizeCalculator(amplifier, samplingRate, channelNumber, recordingTime):
	adc = 24;
	if amplifier.upper() == "BRAINAMP":
		adc = 16;

	return (adc *samplingRate * channelNumber * recordingTime*60 /8 /1024 /1024)

amplifier = input("Amplifier Name: ")
samplingRate = int(input("samplingRate (Hz): "))
channelNumber = int(input("channelNumber: "))
recordingTime  = float(input("recordingTime (mins): "))
fileSize = FileSizeCalculator(amplifier, samplingRate, channelNumber, recordingTime);
print ("The total size of recording is :" + str(fileSize) + " MB")