import pandas as pd
from nba_api.stats.endpoints import playercareerstats, commonallplayers
from nba_api.stats.static import players

# print(players.find_players_by_first_name('kobe'))
# print(players.find_players_by_last_name('jordan'))

playerList = commonallplayers.CommonAllPlayers()
df_playerList = playerList.common_all_players.get_data_frame()
person_id = df_playerList['PERSON_ID']
df_playerList.set_index("PERSON_ID", inplace=True)

df_all_playerprofile = pd.DataFrame()
df_active_playerprofile = pd.DataFrame()
df_retire_playerprofile = pd.DataFrame()

for id in person_id:
    playerprofile = playercareerstats.PlayerCareerStats(player_id=id)
    df_playerprofile = playerprofile.career_totals_regular_season.get_data_frame()
    player_name = df_playerList.loc[id]['DISPLAY_FIRST_LAST']
    df_playerprofile.insert(0, "NAME", player_name, True)
    print(df_playerprofile)
    df_all_playerprofile = pd.concat([df_all_playerprofile, df_playerprofile], axis=0, ignore_index=True)

    if df_playerList.loc[id]['ROSTERSTATUS'] == 1:
        df_active_playerprofile = pd.concat([df_active_playerprofile, df_playerprofile], axis=0, ignore_index=True)

    else:
        df_retire_playerprofile = pd.concat([df_retire_playerprofile, df_playerprofile], axis=0, ignore_index=True)

df_all_playerprofile = df_all_playerprofile.drop(columns=['LEAGUE_ID', 'Team_ID'])
df_all_playerprofile_without_name = df_all_playerprofile.drop(columns=['NAME'])
df_active_playerprofile = df_active_playerprofile.drop(columns=['LEAGUE_ID', 'Team_ID'])
df_retire_playerprofile = df_retire_playerprofile.drop(columns=['LEAGUE_ID', 'Team_ID'])

print(df_all_playerprofile)
print(df_all_playerprofile_without_name)
print(df_active_playerprofile)
print(df_retire_playerprofile)

df_all_playerprofile.to_csv('dataset/career_totals_regular_season_all.tsv', sep='\t', index=False)
df_all_playerprofile_without_name.to_csv('dataset/career_totals_regular_season_all_without_name.tsv', sep='\t', index=False)
df_active_playerprofile.to_csv('dataset/career_totals_regular_season_active.tsv', sep='\t', index=False)
df_retire_playerprofile.to_csv('dataset/career_totals_regular_season_retire.tsv', sep='\t', index=False)
