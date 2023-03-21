# import bookmakers.xbit as xbit
# import log
# competitions = [
# 	{'sport': "football", 'competition': "ligue1"},
# 	{'sport': "football", 'competition': "liga"},
# 	{'sport': "football", 'competition': "LDC"},
# 	{'sport': "football", 'competition': "europa"},
# 	{'sport': "football", 'competition': "world"},
# 	{'sport': "football", 'competition': "bundesliga"},
# 	{'sport': "football", 'competition': "premier-league"},
# 	{'sport': "football", 'competition': "serie-a"},
# #	{'sport': "football", 'competition': "primeira"},
# #	{'sport': "football", 'competition': "serie-a-brasil"},
# #	{'sport': "football", 'competition': "a-league"},
# #	{'sport': "football", 'competition': "bundesliga-austria"},
# #	{'sport': "football", 'competition': "division-1a"},
# #	{'sport': "football", 'competition': "super-lig"},
# 	# {'sport': "basketball", "competition": "nba"},
# #	{'sport': "basketball", "competition": "euroleague"},
# ]

# for competition in competitions:
#     a=xbit.get_games(competition)
#     print(a)
import datetime

a={'team1': 'ParisSG', 'team2': 'Lille', 'odds': [1.24, 5.8, 11.0], 'date': datetime.date(2021, 10, 29)}

date=a['date']
b=datetime.date(2021,3,2)
print (date)
print(b)
delta=date-b
print(delta)
delta=str(delta).split(",")[0]
print(delta)