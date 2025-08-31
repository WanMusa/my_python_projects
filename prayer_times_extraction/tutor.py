import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)

df_warriors=df_teams[df_teams['nickname']=='Warriors']

id_warriors=df_warriors[['id']].values[0][0]

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

gamefinder.get_json()
games = gamefinder.get_data_frames()[0]
print(games.head())
     
