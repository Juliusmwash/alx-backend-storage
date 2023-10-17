#!/usr/bin/env python3
"""
This module defines a script that provides some stats about
Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

"""
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f'{status_check} status check')
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
