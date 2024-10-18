# to run this app type flask --app app run into the terminal
# flask run also works
from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, world!</p>"
    # insert html code here or a html file

@app.route("/")
def hello():
    # return 'Index Page'
    return render_template('index.html')

# @app.route("/createSticky")
# def hello():
#     return 'Hello world'