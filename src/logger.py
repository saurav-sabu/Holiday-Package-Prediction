import logging
import os
from datetime import datetime

# Create a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path where the log file will be stored
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# Create the directory for log files if it doesn't exist
os.makedirs(log_path,exist_ok=True)

# Complete path for the log file
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH, # Path to the log file
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log message format
    level=logging.INFO # Set the logging level to INFO
)