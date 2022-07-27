import logging
from datetime import datetime
import os
from re import L

LOG_DIR = "housing_logs"
CURRENT_TIMEsTAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME = f"log_{CURRENT_TIMEsTAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)
logging.basicConfig(filename=LOG_FILE_PATH,
        filemode="a",
        format= "[%(asctime)s---%(levelname)s----%(module)s]===>%(message)s)",
        level = logging.INFO)