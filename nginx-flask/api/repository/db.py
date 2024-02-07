# from elasticsearch import Elasticsearch
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


# client = Elasticsearch(
#     "https://localhost:9200",  # Elasticsearch endpoint
#     ca_certs="ca.crt",
#     basic_auth=("elastic", os.environ.get("ELASTIC_PASSWORD")),
# )


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://root:pass@mongodb:27017/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["accounts"]


def get_collection():
    dbname = get_database()

    collection = dbname.get_collection("users")

    return collection


def get_all_docs():
    dbname = get_database()

    collection = dbname.get_collection("users")
    results = collection.find()
    print(results)
    return results
