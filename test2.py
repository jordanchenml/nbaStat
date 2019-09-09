import nba_py
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from nba_py.constants import CURRENT_SEASON
from nba_py import game
from nba_py import player
from nba_py import team
from nba_py.player import PlayerList, PlayerGeneralSplits, PlayerGameLogs

conn = psycopg2.connect(database="NBAstat", user="jordanchen", password="pass123", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()
#cur.execute(''' select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA ='testdb' and TABLE_NAME ='playerlist';''')
#cur.execute('''create table playerlist (
cur.execute('''create table if not exists playerlist (
        index int,
        "PERSON_ID"  int,
        "DISPLAY_LAST_COMMA_FIRST"    varchar(80),
        "DISPLAY_FIRST_LAST"    varchar(80),
        "ROSTERSTATUS"    int,
        "FROM_YEAR"   int,
        "TO_YEAR" int,
        "PLAYERCODE"  varchar(80),
        "TEAM_ID" bigint,
        "TEAM_CITY"   varchar(80),
        "TEAM_NAME"   varchar(80),
        "TEAM_ABBREVIATION"   varchar(80),
        "TEAM_CODE"   varchar(80),
        "GAMES_PLAYED_FLAG"   varchar(80));''')
print ("Table created successfully")


conn.commit()
conn.close()

#pid = player.get_player('LeBron', 'James')
#print(pid)
#print('============================================================\n')
#print('============================================================\n')
#print('============================================================\n')

james = player.PlayerCareer(player_id=2544, per_mode='PerGame', league_id='00').all_star_season_totals()

print(james)

print('============================================================\n')
print('============================================================\n')
print('============================================================\n')

all_players = PlayerList(league_id='00', season='2017-18', only_current=1)
all_players_df = pd.DataFrame(all_players.info())


engine = create_engine('postgresql+psycopg2://jordanchen:pass123@localhost:5432/NBAstat')
all_players_df.to_sql('playerlist', engine, if_exists='append')


#rows = all_players_df.shape[0]
#for i in range(rows):
#    print(all_players_df.info[i])
#for player in all_players.info():
#    print (player)

boxscore_summary = game.BoxscoreSummary("0021800052")
print(boxscore_summary.season_series())
