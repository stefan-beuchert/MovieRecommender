import os
import inspect
import pymongo
import pandas as pd


def get_data(source):
    # source can be a function that connects to mongo db
    if type(source) == pymongo.collection.Collection:
        return pd.DataFrame(list(source.find()))
    # or source can be a path to a local .csv
    return pd.read_csv(source)


def save_data(database_collection, data):
    # delete existing documents
    database_collection.delete_many({})
    database_collection.insert_many(data.to_dict('records'))

    ## if u want to save to a file
    # if os.path.isfile(target):
    #     os.remove(target)
    # data.to_csv(target)


def add_new_data_to_db(database_collection, new_data):
    database_collection.insert_one(new_data)


def delete_data_from_db(database_collection, label_name, data_label):
    database_collection.delete_one({label_name: data_label})


def connect_to_db(db_url, db_name):
    mongo_client = pymongo.MongoClient(db_url)
    return mongo_client[db_name]
