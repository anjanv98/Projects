import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/about')
def hello():
    return 'This is my 1st container image'\
    
@app.route('/version')
def version():
    return 'Version V2'\

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)