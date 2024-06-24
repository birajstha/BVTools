import logging

# Create a logger object with the name of your app
logger = logging.getLogger(f'BirajTools')

# Set the logging level to INFO (or any other level you prefer)
logger.setLevel(logging.INFO)

# Create a file handler to write the log messages to a file
handler = logging.FileHandler('BirajTools.log')

# Create a formatter to specify the format of the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the file handler
handler.setFormatter(formatter)

# Add the file handler to the logger object
logger.addHandler(handler)