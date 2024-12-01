import pymongo
import yaml
from constants import CONFIG_YAML
from loguru import logger
from pathlib import Path
import pprint
from collections.abc import MutableMapping

# Load config file
with open(CONFIG_YAML, "r") as file:
    config = yaml.safe_load(file)

# MongoDB connection
client = pymongo.MongoClient(config["connection_str"])
db = client[config["db_name"]]
team = 'Manchester City'

# top scorers for a team
for i in db.goals.find({"owner.currentTeam.name":team}):
    pprint.pprint(i)

# top assisters for  a team
for i in db.goal_assist.find({"owner.currentTeam.name":team}):
    pprint.pprint(i)


client.close()