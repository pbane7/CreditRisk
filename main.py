from CreditRisk.configure.mongo_db_connection import MongoDBClient
from CreditRisk.exception import CRException

import os, sys


if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print("coll:",mongodb_client.database.list_collection_names())
    