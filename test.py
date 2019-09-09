import nba_py
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from nba_py.constants import CURRENT_SEASON
from nba_py import game
from nba_py import player
from nba_py import team
from nba_py.player import PlayerList, PlayerGeneralSplits, PlayerGameLogs


james = player.PlayerCareer(player_id=2544, per_mode='PerGame', league_id='00').all_star_season_totals()

print(james)

#print('============================================================\n')
#print('============================================================\n')
#print('============================================================\n')

#all_players = PlayerList(league_id='00', season='2017-18', only_current=1)
#all_players_df = pd.DataFrame(all_players.info())



playervsplayer = player.PlayerVsPlayer(player_id=2544, vs_player_id=201935, team_id=1610612739, measure_type='Advanced', 
	per_mode='PerGame',	plus_minus='N', pace_adjust='N', rank='N', league_id='00', season='2017-18', 
	season_type='Regular Season', po_round='0', opponent_team_id='1610612745', period='0')
playervsplayer_df = pd.DataFrame(playervsplayer.on_off_court())
print(playervsplayer_df)

