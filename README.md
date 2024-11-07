# The Emo-board: DECO3000 Prototype
This is for the DECO3000 Designing Intelligent Systems course. Our AI app aims to address mental health by providing a platform where users can vent their thoughts and feelings, as well as seek guidance from our AI about the emotions they are feeling based on their described experiences.

## Table of Contents
1. [Setup on local machine](#setup)
2. [API Key](#api)
3. [Deploy app on local machine](#deploy)
4. [Hardware & Software](#requirements)
5. [Troubleshooting](#troubleshooting)

## Set up the app on a local machine <a id="setup"></a>
1. Ensure that you have Python Version 3.9.2 installed and ready to use
2. Using your preferred code editor, use the terminal and type `git clone https://github.com/vawklee/DECO3000_Prototype.git` to clone the GitHub Repository
3. Create a virtual environment by typing `python3 -m venv venv` in the terminal
4. Activate the virtual environment by typing `. venv/bin/activate`. Refer [here](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) for information about virtual environments in Python
5. Type `pip install -r requirements.txt` into the terminal to install all dependencies in your environment

OR 

6. Set up the required libraries by typing the following commands into your terminal:

    6.1 `pip install python-dotenv`
    <br>6.2 `pip install flask`
    <br>6.3 `pip install requests`
    <br>6.4 `pip install textblob`

### API Key Requirements <a id="api"></a>
This project requires a Wordware API key. For the purposes of this assignment submission, the API key will be included in a .txt file that can be found in the .zip submission folder. 

To set up the API key for use in this project:
1. Create a `.env` file in your cloned GitHub Repository folder containing the project files
2. Copy the API key from the .txt file
3. Paste it into your .env file in the following format: `API_KEY = paste api key here` (do not include quotation marks)

## Deploy app on a local machine <a id="deploy"></a>
1. Ensure that you have followed the instructions listed under 
2. To run the app, type `flask run` into the terminal
3. The app can be viewed at http://127.0.0.1:5000/ (Port number may vary, refer to the terminal for any differences)
4. Exit the app at any time by pressing `Control + C` in your terminal

DISCLAIMER: When using the app and clicking the button `Process sticky-notes`, the web app may take a minute or two to generate and load the output; This wait time is normal (Wordware is slow), DO NOT click the button again to try and generate more than 1 response at a time.

## Hardware & Software for Viewing <a id="requirements"></a>
This app has been developed and tested primarily using Google Chrome & Firefox as the web browser. 

The optimal viewing resolution is currently 2256px x 1504px on a laptop or desktop monitor. Similar screen sizes will produce the same results, however, the current prototype is not responsive thus smaller screen sizes may produce unintended results.

## Troubleshooting <a id="troubleshooting"></a>
If at any time there are issues with parts of the website not responding or producing errors, try the following steps. This is not a definitive list of troubleshooting steps, but can provide some guidance towards fixing issues:

1. Press `Control + C` in your terminal to stop the server
2. Close the webpage
3. Type `flask run` to start the server again and re-visit the link at http://127.0.0.1:5000/ (Port number may vary, refer to the terminal for any differences)

### Waiting for the app to generate an output after clicking "Process sticky-notes"? 
Wordware may take a few minutes to generate a response in the background, please wait for a minute or two and see if output loads.

Otherwise if there is a backend error or nothing is outputted, it is very likely that we have run out of Wordware credit and cannot generate anymore AI responses. 