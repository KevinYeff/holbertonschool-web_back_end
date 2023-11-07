#!/usr/bin/env python3
"""Task 9 Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document in a collection based on kwargs
    Parameters:
        mongo_collection: A MongoDB collection
        @**kwargs: Parameters of the new document
    Return: id of the new document"""
    if mongo_collection:
        return mongo_collection.insert_one(kwargs).inserted_id
