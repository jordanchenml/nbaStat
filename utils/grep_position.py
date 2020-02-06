from nba_api.stats.endpoints import commonplayerinfo


print(commonplayerinfo.CommonPlayerInfo(player_id=893).get_normalized_dict()['CommonPlayerInfo'][0]['POSITION'])
