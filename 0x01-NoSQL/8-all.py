#!/usr/bin/env python3
""" List all documents in MongoDB collection """

def list_all(mongo_collection):
    """ Return all documents in a collection or an empty list if none """
    return list(mongo_collection.find()) if mongo_collection else []
