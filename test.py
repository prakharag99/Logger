import requests

# Defining the base URL for the Flask API running locally
BASE_URL = 'http://127.0.0.1:5000'

def test_log_event(message, log_type, severity, metadata=None):

    # Defining the log data to be sent in the POST request
    log_data = {
        "message": message,
        "type": log_type,
        "severity": severity,
        "metadata": metadata
    }

    # Sending a POST request to log the event
    response = requests.post(f"{BASE_URL}/log/transmission", json=log_data)

    print(f"Log Event Response for {log_type}:", response.json())

def test_get_logs():

    # Sending a GET request to retrieve all logs
    response = requests.get(f"{BASE_URL}/log/retrieval")
    print("Get Logs Response:", response.json())

def test_filter_logs(category, value):

    # Sending a GET request to filter logs based on category and value
    response = requests.get(f"{BASE_URL}/log/filter?category={category}&value={value}")
    print(f"Filtered Logs Response for {category}={value}:", response.json())

if __name__ == "__main__":

    # Testing logging events, messages, and errors using a loop
    for i in range(1, 10, 5):
        test_log_event(f"Test event {i}", "EVE", "INFO", {"key": f"value {i}"})
        test_log_event(f"Test error {i+1}", "ERR", "DEBUG", {"key": f"value {i+1}"})
        test_log_event(f"Test message {i+2}", "MSG", "WARNING", {"key": f"value {i+2}"})
        test_log_event(f"Test error {i+3}", "ERR", "CRITICAL", {"key": f"value {i+3}"})
        test_log_event(f"Test message {i+4}", "MSG", "INFO", {"key": f"value {i+4}"})

    # Testing retrieving all logs
    test_get_logs()

    # Printing separator lines to distinguish between different sets of tests
    print("-------------------------------")

    # Testing filtering logs by type
    test_filter_logs("type", "ERR")

    print("-------------------------------")

    # Testing filtering logs by severity
    test_filter_logs("severity", "CRITICAL")

    print("-------------------------------")
    print("-------------------------------")
