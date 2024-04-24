# Logger System:

This project provides a simple log management system implemented using Flask for the API backend and Python for the logger functionality.

## Overview

The system consists of two main components:

1. *app.py*: This file contains the Flask application responsible for handling HTTP requests and responses. It exposes endpoints for logging events, retrieving logs, and filtering logs based on category and value.

2. *logger.py*: This file contains the Logger class, which is responsible for logging events, maintaining a circular linked list of log entries, and filtering log entries based on category and value.

3. API endpoints in *app.py*:
   a. '/log/transmission' - for storing the data in the circular linked list.
   b. '/log/retrieval' - for logging all teh data to the console/command line.
   c. '/log/filter' - for retrieving logs according to filters specified by the user in *test.py*

## Setup
1. Clone the repo using: git clone https://github.com/prakharag99/Logger
2. Install the required dependencies using pip:

    pip install flask

    Rest pre-installed libraries: json, datetime, requests, jsonify
    Note: use pip install to install them if not pre-installed.
    
3. Run the Flask application in the following order:

    run the *logger.py* file.
    *python app.py* OR just run the code
    *python test.py* to run the test file. Note: Do this in a new terminal

## Some conventions/restrictions/limitations of the system:

1. For the type of logged text, I have classified it into: error (ERR), event (EVE) and message (MSG).

2. The severity of the logged text is classified as: debug, critical, warning and info.

3. The mapping of the type of text logged and severity is as follows:

   a. error (ERR) -> debug, critical
   b. message (MSG) -> warning, info
   c. event (EVE) -> info

