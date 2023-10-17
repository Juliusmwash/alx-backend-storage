#!/usr/bin/env python3
"""
This module defines a function 'insert_school'
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function for inserting a new document in a collection based on kwargs
    """
    _id = mongo_collection.insert(kwargs)
    return _id
