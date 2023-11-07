#!/usr/bin/env python3
"""Task 11 Where can I learn Python"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns a list of schools that have a specific topic
    Parameters:
        @mongo_collection: A MongoDB collection
        @topic: String, topic to search for"""
    return mongo_collection.find({"topics": topic})
