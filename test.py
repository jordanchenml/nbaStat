# from nba_api.stats.endpoints import commonplayerinfo
# # from nba_api.stats.library import http

# # print(http.STATS_HEADERS)
# # Basic Request
# # player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)


# custom_headers = {
#     'Host': 'stats.nba.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Referer': 'https://stats.nba.com/',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'x-nba-stats-origin': 'stats',
#     'x-nba-stats-token': 'true'
# }

# # Only available after v1.1.0
# # Proxy Support, Custom Headers Support, Timeout Support (in seconds)
# player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)

# print(player_info)




import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder, teamyearbyyearstats

# Define what years to collect game data on
years = ["2015-16",
        "2016-17",
        "2017-18",
        "2018-19",]

# Get dataframe of games
games = pd.DataFrame()
for y in years:
    print("Getting games for {}...    ".format(y), end='', flush=True)
    g = leaguegamefinder.LeagueGameFinder(
            player_or_team_abbreviation="T",
            league_id_nullable="00",
            season_type_nullable="Regular Season",
            season_nullable=y,
            )
    print("Done!")
    g_df = g.league_game_finder_results.get_data_frame()
    g_df["YEAR"] = y
    games = games.append(g_df)
    
    career = playercareerstats.PlayerCareerStats(player_id='203076')

# Filter out relevent columns
games = games[["GAME_ID", "TEAM_ID", "MATCHUP", "GAME_DATE", "WL", "YEAR"]]

# Find team ids
team_ids = list(g_df["TEAM_ID"].unique())

# Get team stat for all years
team_stats = pd.DataFrame()
for t in team_ids:
    print("Getting team stats for {}...   ".format(t), end='', flush=True)
    stats = teamyearbyyearstats.TeamYearByYearStats(
            league_id="00",
            per_mode_simple="Totals",
            season_type_all_star="Regular Season",
            team_id=t,
            )
    print("Done!")
    stats_df = stats.team_stats.get_data_frame()
    team_stats = team_stats.append(stats_df)


# Merge the stats into vertical pd of games
games_vertical_stats = pd.merge(left=games, right=team_stats, how='inner', on=["TEAM_ID","YEAR"])

# Get the first and last match data
dup1 = games_vertical_stats.drop_duplicates('GAME_ID', 'first')
dup2 = games_vertical_stats.drop_duplicates('GAME_ID', 'last')

# Drop columns that describe the same data
dup2 = dup2.drop(["MATCHUP"], axis=1)
dup2 = dup2.drop(["WL"], axis=1)

# Merge vertical stats of the two games
game_team_stats = pd.merge(dup1, dup2, on="GAME_ID")

print("\n")
print(game_team_stats.head())
print()
print(game_team_stats.columns)