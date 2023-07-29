import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True) ## keep appending the log files to that folder if it already exists.

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ", 
    level=logging.INFO
    )

if __name__ == "__main__":
    logging.info("This is a sample log test")