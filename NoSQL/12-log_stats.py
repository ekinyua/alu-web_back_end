#!/usr/bin/env python3
"""python scripts"""
from pymongo import MongoClient
from os import getenv

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection, option=None):
    """ script that provides some stats about Nginx logs stored in MongoDB
    """
    if option:
        value = mongo_collection.count_documents(
            {"method": option})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents({})
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    try:
        mongo_url = getenv("MONGO_URL", "mongodb://127.0.0.1:27017")
        client = MongoClient(mongo_url)
        nginx_collection = client.logs.nginx
        log_stats(nginx_collection)
    except Exception as e:
        print(f"An error occurred: {e}")
