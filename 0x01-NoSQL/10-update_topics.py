#!/usr/bin/env python3
""" Update document topics """

def update_topics(mongo_collection, name, topics):
    """ Update all topics of a school document """
    mongo_collection.update_many({ "name": name }, { "$set": { "topics": topics } })
