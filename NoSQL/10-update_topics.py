#!/usr/bin/env python3
"""Task 10 Change school topics"""


def update_topics(mongo_collection, name, topics):
    """Functionj that changes topics of a school document based on the name
    Parameters:
        @mongo_collection: A MongoDB collection
        @name: String; school name to update
        @topics: List of strings; list of topics approached in the school"""
    if mongo_collection:
        mongo_collection.update_many({"name": name},
                                     {"$set": {"topics": topics}})
