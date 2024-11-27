import pymongo
import json
import yaml
from constants import CONFIG_YAML, ROOT_DIR
from loguru import logger
from pathlib import Path

# Load config file
with open(CONFIG_YAML, "r") as file:
    config = yaml.safe_load(file)

# MongoDB connection
client = pymongo.MongoClient(config["connection_str"])
db = client[config["db_name"]]
collection = db[config["collections"][0]]

# Load JSON data from file
with open(Path(ROOT_DIR / "fixtures/fixtures.json")) as file:
    jsonObj = json.load(file)

# Insert data
if isinstance(jsonObj, list):
    result = collection.insert_many(jsonObj)  # Handle array of JSON objects
else:
    result = collection.insert_one(jsonObj)  # Handle single JSON object

logger.success(f"Inserted document IDs: {result.inserted_ids}")

client.close()
