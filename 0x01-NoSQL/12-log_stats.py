#!/usr/bin/env python3
""" Provide stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count the total number of logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Count the number of requests by each HTTP method
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of GET requests to /status
    status_check_count = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")
