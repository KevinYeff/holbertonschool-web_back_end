#!/usr/bin/env python3
"""Task 8 List all documents in Python"""


def list_all(mongo_collection):
    """Function that lists all documents from a MongoDB collection
    Parameters:
        mongo_collection: A MongoDB Collection
    Return:
        Returns: A list of documents in a collection, otherwise
        returns an empty list"""

    if mongo_collection:
        return mongo_collection.find()
    else:
        return []
