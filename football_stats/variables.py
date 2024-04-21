'''
we will import some player
info(id, jersey_number, team, name, matches)
from this file

tables with process of finding
this info in finder.ipynb
'''

from mplsoccer import Sbopen
parser = Sbopen()

df_matches = parser.match(competition_id=7, season_id=235)
comp_name = f'{df_matches.competition_name.iloc[0]}, {df_matches.season_name.iloc[0]}'

cur_team = 'Paris Saint-Germain'
cur_team_m = df_matches[(df_matches['home_team_name'] == cur_team) | (df_matches['away_team_name'] == cur_team)]
cur_team_m_arr_ids = list(cur_team_m.match_id)

player_matches_ids = []
player_iden = 4320 #Neymar jr.
for i_id in cur_team_m_arr_ids:
    match_lineup = parser.lineup(int(i_id))
    if match_lineup['player_id'].isin([player_iden]).any():
        player_matches_ids.append(i_id)

player_matches = cur_team_m[cur_team_m['match_id'].isin(player_matches_ids)]

df = parser.lineup(player_matches_ids[0])
player_nn = df.player_nickname[df.player_id == player_iden].iloc[0]
player_number = df.jersey_number[df.player_id == player_iden].iloc[0]