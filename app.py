# to run this app type flask --app app run into the terminal
# flask run also works
from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, world!</p>"
    # insert html code here or a html file

@app.route("/")
#def hello():
def index():
    # return 'Index Page'
    return render_template('index.html')

# @app.route("/createSticky")
# def hello():
#     return 'Hello world'
#to analyse user input 
@app.route("/analyse", methods=['POST'])
def analyse():
    user_input = request.form.get('user_input', '')# to get user input from the sticky note 
    if user_input:
        #handling sentiment analysis using TextBlob 
        blob = TextBlob(user_input)
        polarity =blob.sentiment.polarity
        #This is where I am determining what is the benchmarks of a positrive, negative and neutral sentiment
        #The polarity score is a float within the range [-1.0, 1.0]
        if polarity >0:
            sentiment = 'positive'
