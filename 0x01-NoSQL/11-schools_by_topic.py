#!/usr/bin/env python3
"""
This module defines a function 'schools_by_topic'
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school having a specific topic.
    mongo_collection will be the pymongo collection object.
    topic (string) will be topic searched.
    """
    schools = mongo_collection.find({"topics": topic})
    schools_list = [i for i in schools]
    return schools_list
