To Fetch API using NLP

## Setup and Execution Instructions:

1. Install Python (if not already installed) from https://www.python.org/downloads/
2. Install required dependencies using pip:
   pip install Flask
   pip install requests
   pip install vaderSentiment
3. Clone this repository to your local machine or download the files.

## Execution:

1. Navigate to the directory where the files are located.
2. Run the Flask application by executing the following command in the terminal or command prompt:
    python app.py
3. Once the server is running, open a web browser and go to http://127.0.0.1:5000/ to access the application.

## Usage:

1. The application fetches data from an API endpoint and performs sentiment analysis on text data.
2. Click the "Fetch Data" button to retrieve data from the API.
3. The fetched data will be displayed on the web page in JSON format. (after clicking button wait for sometime to load the data scroll down the data will be sucessfully extracted)


###Note:
There are two app.py and app1.py files, one is by using NLP and another one is without using both are working well.

##How it Works:
1.Flask Application:
The Flask application (app.py) serves the HTML page and handles API requests.
It includes a route to render the main HTML page (index.html) and a route (/fetch_data) to fetch data from the external API.
The main_request function retrieves data from the API.
The get_total_pages function calculates the total number of pages based on the API response.
The parse_json function parses the API response, extracts relevant data, and performs sentiment analysis using the analyze_sentiment function.

2.HTML Template:
The HTML file (index.html) includes a button to fetch data and a section to display the fetched data.
The jQuery script in the HTML file makes an AJAX request to the /fetch_data endpoint when the button is clicked, and displays the JSON response on the page.

3.CSS Styling:
The CSS file (style.css) provides styling for the HTML elements, including the container, button, and background.
