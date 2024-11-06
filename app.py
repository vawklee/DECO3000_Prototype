# to run this app type flask --app app run into the terminal
# flask run also works
import os
import json
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
# Load API_KEY from .env
load_dotenv()
api_key = os.getenv('API_KEY')
# Check if the API key was loaded correctly
if not api_key:
    print("Error: API key not found. Please check your .env file.")
prompt_id = "70deab75-3dfc-4bb2-abb0-81d5c297638e"
app = Flask(__name__)
# Function to call Wordware API
def call_wordware(input_text, sentiment):
    inputs = {
        "user_input": input_text,
        "sentiment": sentiment
    }
    print(f"Sending data to Wordware: {inputs}")  # Debug: Check data being sent
    # print(api_key)
    try:
        prompt_id = "70deab75-3dfc-4bb2-abb0-81d5c297638e"
        # api_key = os.getenv('API_KEY')  # Ensure this is correctly loaded
        print("Starting Wordware API request...")#debugging 
        
        response = requests.post(
           f"https://app.wordware.ai/api/released-app/{prompt_id}/run",
           json={"inputs": inputs},
           headers={"Authorization": f"Bearer {api_key}"},
           stream=True,
                )
        if response.status_code != 200:
            print("Wordware Request failed with status code", response.status_code)
            return {"error": "Wordware API call failed."}
        # Process the streamed response
        output = ""
        for line in response.iter_lines():
            if line:
                content = json.loads(line.decode("utf-8"))
                value = content["value"]
                if value["type"] == "chunk":
                    output += value["value"]

        # Debugging: Log the output received from Wordware
        print(f"Wordware response output: {output}")
        return {"response": output}

    except Exception as e:
        print(f"Error calling Wordware: {str(e)}")
        return {"error": f"Internal error: {str(e)}"}
# @app.route("/")
# def hello_world():
#     return "<p>Hello, world!</p>"
    # insert html code here or a html file

@app.route("/")
#def hello():
def index():
    if request.method == 'POST':
        # Handle POST request here, if needed
        pass
    return render_template('index.html')

# @app.route("/createSticky")
# def hello():
#     return 'Hello world'
#to analyse user input 
@app.route("/analyse", methods=['POST'])
def analyse():
    try:
        print("Received a POST request on /analyse")  # Debugging log
        data = request.get_json()# get Json data from the request
        print(f"Received JSON data: {data}")  # Log the data received for debugging
        if not data:
            return jsonify({'error':'No JSON data received'}), 400
        user_input = data.get('user_input', '')# to get user input from the sticky note 
        print(f"User input: {user_input}")  # Log the user input received for debugging
        if user_input:
        #handling sentiment analysis using TextBlob 
            blob = TextBlob(user_input)
            polarity =blob.sentiment.polarity
        #This is where I am determining what is the benchmarks of a positrive, negative and neutral sentiment
        #The polarity score is a float within the range [-1.0, 1.0]
            if polarity >0:
                sentiment = 'positive'
            elif polarity <0:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'
            #return whatever the result of this sentiment analysis as usable input to feed into the LLM 
            #creating a disctionary 
            # Call Wordware with the input and sentiment
            wordware_result = call_wordware(user_input, sentiment)

            # Return the result along with the sentiment analysis
            result = {
                'input': user_input,
                'sentiment': sentiment,
                'wordware_response': wordware_result
            }
            return jsonify(result)

        return jsonify({'error':'No input provided'}), 400
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
if __name__ == "__main__":
            app.run(debug=True) 