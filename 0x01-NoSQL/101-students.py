#!/usr/bin/env python3
"""
This module defines the function 'top_students'
"""


def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score.
    pymongo collection object.
    The top must be ordered.
    The average score must be part of each item returns with
    key = averageScore.
    """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
