from flask import Flask


app = Flask(__name__)

@app.route('/', methods= ["POST"])
def index():
    return "Hello people"


if __name__ == "__main__":
    app.run()