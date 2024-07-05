#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

def log_stats():
    """Calculate and display stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    # Status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
