from flask import Flask
from Housing.logger import logging
import sys
from Housing.exception import HousingException

app = Flask(__name__)

@app.route('/', methods= ["POST","GET"])
def index():
    try:
        raise Exception("we are testing the Exception module")
    except Exception as e:
        housing = HousingException(e, sys)
        print(housing.error_message)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
        return "Hello people"


if __name__ == "__main__":
    app.run()