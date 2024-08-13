#!/usr/bin/env python3
"""
Module: Task 10.
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of collection's document based on name."""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
