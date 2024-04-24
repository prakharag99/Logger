from flask import Flask, request, jsonify
from logger import Logger

app = Flask(__name__)

# Here I'm initializing a Logger instance
logger = Logger()

@app.route('/log/transmission', methods=['POST'])
def log_event():

    """
    Here I am logging an event with the provided data.
    """
    # Extracting data from the JSON request
    data = request.json
    message = data.get('message')
    log_type = data.get('type', 'INFO')
    severity = data.get('severity', 'INFO')
    metadata = data.get('metadata')
    logger.log(message, log_type=log_type, severity=severity, metadata=metadata)

    # Returning a JSON response indicating the success of the log entry
    return jsonify({'message': 'Log entry added successfully'}), 201

@app.route('/log/retrieval', methods=['GET'])
def get_logs():
    """
    Here I am getting all logs.
    """
    # Initializing an empty list to store log entries
    logs = []
    current_node = logger.log_entries.head
    while current_node:
        logs.append(current_node.log_entry)
        current_node = current_node.next
        if current_node == logger.log_entries.head:
            break

    # Returning the list of log entries as a JSON response
    return jsonify(logs), 200

@app.route('/log/filter', methods=['GET'])
def get_filtered_logs():

    """
    Here I am getting filtered logs based on category and value parameters.
    """
    # Extracting the category and value parameters from the request query
    category = request.args.get('category')  # Type or severity
    value = request.args.get('value')  # Value to filter
    if not category or not value:
    
        return jsonify({'error': 'Please provide both category and value parameters'}), 400
    
    filtered_logs = logger.filter_logs(category, value)

    # Returning the filtered logs as a JSON response
    return jsonify(filtered_logs), 200

if __name__ == '__main__':
    app.run(debug=True)
