#!/usr/bin/env python3
""" Provide stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: {collection.count_documents({'method': method})}")
    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")
