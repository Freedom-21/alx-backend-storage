#!/usr/bin/env python3
""" Return schools having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """ Find schools having the specified topic """
    return list(mongo_collection.find({ "topics": topic }))
