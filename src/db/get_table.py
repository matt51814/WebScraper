import pymongo
import yaml
from constants import CONFIG_YAML
from loguru import logger
from pathlib import Path
import pprint
from collections.abc import MutableMapping

def _flatten_dict_gen(d: MutableMapping, parent_key: str, sep: str):
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            yield from flatten_dict(v, new_key, sep=sep).items()
        else:
            yield new_key, v

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str = '.') -> MutableMapping:
    """ Flatten nested dictionaries """
    return dict(_flatten_dict_gen(d, parent_key, sep))


def find(db: pymongo.MongoClient, collection_name: str, cols: dict[str, int]) -> dict[str, list[int | str | float]]:
    """
    Retrieve data from MongoDB and convert to a format that can create DataFrames
    
    Args:
        db: MongoDB Client containing data
        collection_name: name of collection you wish to query
        cols: list of items you wish to return from collection
    
    Returns:
        results: resulting dictionary that can be easily turned into a DataFrame
    """
    collection = db[collection_name]
    results = {c: [] for c in cols}
    for post in collection.find({}, cols):
        for c in cols:
            results[c].append(flatten_dict(post)[c])
    return results

# Load config file
with open(CONFIG_YAML, "r") as file:
    config = yaml.safe_load(file)

# MongoDB connection
client = pymongo.MongoClient(config["connection_str"])
db = client[config["db_name"]]
cols = {
    "team.club.name": 1,
    "overall.played": 1,
    "overall.won": 1,
    "overall.drawn": 1,
    "overall.lost": 1,
    "overall.goalsFor": 1,
    "overall.goalsAgainst": 1,
    "overall.goalsDifference": 1,
    "overall.points": 1,
    "home.played": 1,
    "home.won": 1,
    "home.drawn": 1,
    "home.lost": 1,
    "home.goalsFor": 1,
    "home.goalsAgainst": 1,
    "home.goalsDifference": 1,
    "home.points": 1,
    "away.played": 1,
    "away.won": 1,
    "away.drawn": 1,
    "away.lost": 1,
    "away.goalsFor": 1,
    "away.goalsAgainst": 1,
    "away.goalsDifference": 1,
    "away.points": 1
}
results = find(db=db, collection_name="standings", cols=cols)
pprint.pprint(results)
client.close()
