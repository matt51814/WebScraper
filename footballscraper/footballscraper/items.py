# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass
from datetime import datetime


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


@dataclass
class RecentMatchesItem:
    date: datetime
    home_team: str
    away_team: str
    home_score: int
    away_score: int    
    odds: str    

@dataclass
class NextMatchesItem:
    date: datetime
    home_team: str
    away_team: str 
    odds: str    


@dataclass
class ScorersItem:
    team: str
    player: str
    scorer_points: int
    goals: int
    assists: int
    soccer_points_per_match: float
    goals_per_match: float
    avg_minutes_to_score_or_assist: float
    avg_minutes_to_score: float
