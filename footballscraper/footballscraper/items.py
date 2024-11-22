# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass


class FootballscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


@dataclass
class StandingItem:
    pos: str
    team: str
    matches: int
    points: int
    plus_and_minus: int
    goals: str
