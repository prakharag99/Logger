from datetime import datetime
import json

# Defining a global variable to control the maximum size of the circular linked list
MAX_LOG_SIZE = 8

class LogNode:
    def __init__(self, log_entry):

        # I have initialized a LogNode with the log entry
        self.log_entry = log_entry
        self.next = None

class CircularLinkedList:
    def __init__(self):

        # Initializing a CircularLinkedList with head, tail, and size attributes
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, log_entry):

        # Appending a new log entry to the circular linked list
        new_node = LogNode(log_entry)

        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def remove_oldest(self):

        # Here I'm removing the oldest log entry from the circular linked list if it exceeds the maximum size

        if self.size > MAX_LOG_SIZE:
            self.head = self.head.next
        
            self.tail.next = self.head
            self.size -= 1

class Logger:
    def __init__(self):

        # A Logger with a circular linked list is initialized to store log entries
        self.log_entries = CircularLinkedList()

    def log(self, message, log_type="MSG", severity="INFO", metadata=None):

        # Here I'm logging a new event with the provided data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "type": log_type,
            "severity": severity,
            "message": message,
            "metadata": metadata
        }

        # I convert the log entry to a JSON string and append it to the circular linked list
        json_log_entry = json.dumps(log_entry)
        self.log_entries.append(json_log_entry)

        # Then the oldest log entry is removed if the list exceeds the maximum size
        self.log_entries.remove_oldest()

    def format_log_entry(self, log_entry):

        # Here I'm formatting a log entry into a readable string
        formatted_log = f"[{log_entry['timestamp']}] [{log_entry['type']}] [{log_entry['severity']}] {log_entry['message']}"
        if log_entry['metadata']:
            formatted_log += f" - Metadata: {log_entry['metadata']}"
        return formatted_log

    def display_logs(self):

        # Here I'm displaying all the log entries in the circular linked list
        current_node = self.log_entries.head
        while current_node:
            print(current_node.log_entry)
            current_node = current_node.next
            if current_node == self.log_entries.head:
                break

    def filter_logs(self, category, value):
        
        # Here I'm filtering logs based on the specified category and value
        filtered_logs = []
        current_node = self.log_entries.head
        while current_node:
            log_entry = json.loads(current_node.log_entry)
            if log_entry.get(category) == value:
                filtered_logs.append(log_entry)
            current_node = current_node.next
            if current_node == self.log_entries.head:
                break
        return filtered_logs

