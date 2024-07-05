#!/usr/bin/env python3
"""python scripts"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    """Script that provides some stats about Nginx logs stored in MongoDB."""
    # Total number of log entries
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Status check count
    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    # Connect to the MongoDB server and select the nginx collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Call the log_stats function
    log_stats(nginx_collection)
