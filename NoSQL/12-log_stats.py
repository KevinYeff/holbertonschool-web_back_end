#!/usr/bin/env python3
"""Task 12 Log stats"""
from pymongo import MongoClient


def log_stats():
    """Funcion that provides stats about Nginx logs"""
    # Connect to the database and collection
    client = MongoClient('mongodb://localhost:27017')
    # Database
    db = client.logs
    # Collection
    collection = db.nginx

    # Get the total number of documents in the collection
    # collection.count() is deprecated
    total_logs = collection.count_documents({})

    # Get the number of documents with each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Get the number of documents with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET",
                                               "path": "/status"})

    # Print the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


# Make sure the script is not executed when imported
if __name__ == "__main__":
    log_stats()
