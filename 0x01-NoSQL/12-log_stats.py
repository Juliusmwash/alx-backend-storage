#!/usr/bin/env python3
"""
This module defines a script that provides some stats about
Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def main():
    """
    Connect to MongoDB and provide statistics about Nginx logs.

    This script connects to a MongoDB database and retrieves statistics
    about Nginx logs, including the total number of logs, the count of
    each HTTP method (GET, POST, PUT, PATCH, DELETE), and the count of
    status check logs (GET method with path=/status).

    The results are printed to the console.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    collection = db['nginx']

    # Get the total number of documents in the collection
    total_logs = collection.count_documents({})

    # Get the number of documents with each HTTP method
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in http_methods}

    # Get the number of documents with method=GET and path=/status
    status_check = collection.count_documents(
            {"method": "GET", "path": "/status"})

    # Print the results
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    main()
