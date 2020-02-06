import pandas as pd
from nba_api.stats.endpoints import playercareerstats, commonallplayers, commonplayerinfo
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
df_playerID_mapping = pd.DataFrame()
pair = list()

# person_id = [893, 977, 202689]
for id in person_id:
    # Create id - name pair.
    pair.append([id, df_playerList.loc[id]['DISPLAY_FIRST_LAST']])
    playerprofile = playercareerstats.PlayerCareerStats(player_id=id)
    df_playerprofile = playerprofile.career_totals_regular_season.get_data_frame()
    df_playerprofile.insert(1,
                            "POSITION",
                            commonplayerinfo.CommonPlayerInfo(player_id=id)
                            .get_normalized_dict()['CommonPlayerInfo'][0]['POSITION'],
                            True)
    # player_name = df_playerList.loc[id]['DISPLAY_FIRST_LAST']
    # df_playerprofile.insert(0, "NAME", player_name, True)
    print(df_playerprofile)
    df_all_playerprofile = pd.concat(
        [df_all_playerprofile, df_playerprofile], axis=0, ignore_index=True)

    if df_playerList.loc[id]['ROSTERSTATUS'] == 1:
        df_active_playerprofile = pd.concat(
            [df_active_playerprofile, df_playerprofile], axis=0, ignore_index=True)

    else:
        df_retire_playerprofile = pd.concat(
            [df_retire_playerprofile, df_playerprofile], axis=0, ignore_index=True)

df_playerID_mapping = pd.DataFrame(pair, columns=['PLAYER_ID', 'NAME'])
df_all_playerprofile = df_all_playerprofile.drop(
    columns=['LEAGUE_ID', 'Team_ID'])
df_active_playerprofile = df_active_playerprofile.drop(
    columns=['LEAGUE_ID', 'Team_ID'])
df_retire_playerprofile = df_retire_playerprofile.drop(
    columns=['LEAGUE_ID', 'Team_ID'])

print(df_playerID_mapping)
print(df_all_playerprofile)
print(df_active_playerprofile)
print(df_retire_playerprofile)

df_playerID_mapping.to_csv(
    'dataset/playerID_name_pairs.tsv', sep='\t', index=False)
df_all_playerprofile.to_csv(
    'dataset/career_totals_regular_season_all.tsv', sep='\t', index=False)
df_active_playerprofile.to_csv(
    'dataset/career_totals_regular_season_active.tsv', sep='\t', index=False)
df_retire_playerprofile.to_csv(
    'dataset/career_totals_regular_season_retire.tsv', sep='\t', index=False)
