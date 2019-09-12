import nba_py
import pandas as pd
from nba_py import player, team, game, constants
from time import sleep
import random
import datetime


def get_home_and_guest_TEAM_ID(game_id, season):
    PlayerGeneralSplits = game.BoxscoreSummary(game_id=game_id, season=season, season_type='Regular Season',
                                               range_type='0', start_period='0', end_period='0', start_range='0',
                                               end_range='0').game_summary()
    return PlayerGeneralSplits['HOME_TEAM_ID'], PlayerGeneralSplits['VISITOR_TEAM_ID']


# get_home_and_guest_TEAM_ID('0021701214', '2017-18')

def test():
    return 5
