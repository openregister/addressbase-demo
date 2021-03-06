#!/usr/bin/env python

# import matched school addresses into Mongo

from config import MONGO_URL
from csv import DictReader
from pymongo import MongoClient

client = MongoClient(MONGO_URL)
db = client.get_default_database()

filename = 'school-address.tsv'
filename = '../../school-data/maps/school-address.tsv'
collection = db['school-address']

for doc in DictReader(open(filename), delimiter='\t'):
    if doc['address']:
        collection.insert(doc)

collection.ensure_index('school')
collection.ensure_index('address')
