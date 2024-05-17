import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_INITDB_DATABASE = os.getenv("MONGO_INITDB_DATABASE")
MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")

client = MongoClient(
    host=MONGO_HOST,
    port=27017,
    username=MONGO_INITDB_ROOT_USERNAME,
    password=MONGO_INITDB_ROOT_PASSWORD,
)


db = client[MONGO_INITDB_DATABASE]
user_collection = db["users_affiliate3"]
wallet_collection = db["users_wallet"]
payout_collection = db["payout_affiliate"]
