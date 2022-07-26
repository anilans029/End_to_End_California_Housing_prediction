from flask import Flask
from Housing.logger import logging

app = Flask(__name__)

@app.route('/', methods= ["POST","GET"])
def index():
    logging.info("we are testing logging module")
    return "Hello people"


if __name__ == "__main__":
    app.run()