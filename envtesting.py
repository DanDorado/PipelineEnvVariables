from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def state_name():
    USER = str(os.getenv('USER'))
    LASTNAME = str(os.getenv('LASTNAME'))
    return("The User I have inherited from my local environment is " + USER + ". \n The second name of the user is " + LASTNAME + ". \n")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=1000, debug = True)