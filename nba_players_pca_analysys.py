import pandas as pd
from nba_api.stats.endpoints import playercareerstats, commonallplayers
# Anthony Davis
career = playercareerstats.PlayerCareerStats(player_id='203076')
print(career.career_totals_regular_season.get_data_frame())

playerList = commonallplayers.CommonAllPlayers()
df_playerList = playerList.common_all_players.get_data_frame()
print(df_playerList)
df_playerList.to_csv('playerList.tsv', sep='\t')