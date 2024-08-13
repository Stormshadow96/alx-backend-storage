#!/usr/bin/env python3
"""Module: Task 9."""


def insert_school(mongo_collection, **kwargs):
    """Inserts new document in collection based on kwargs."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
