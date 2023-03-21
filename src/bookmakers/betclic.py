from bs4 import BeautifulSoup
import requests

competition_urls = {
		'football':
		{
			"ligue1": "https://www.betclic.fr/football-s1/ligue-1-uber-eats-c4",
			"liga": "https://www.betclic.fr/football-s1/espagne-liga-primera-c7",
			"bundesliga": "https://www.betclic.fr/football-s1/allemagne-bundesliga-c5",
			"premier-league": "https://www.betclic.fr/football-s1/angl-premier-league-c3",
			"serie-a": "https://www.betclic.fr/football-s1/italie-serie-a-c6",
			"primeira": "https://www.betclic.fr/football-s1/portugal-primeira-liga-c32",
			"serie-a-brasil": "https://www.betclic.fr/football-s1/bresil-serie-a-c187",
			"a-league": "https://www.betclic.fr/football-s1/australie-a-league-c1874",
			"bundesliga-austria": "https://www.betclic.fr/football-s1/autriche-bundesliga-c35",
			"division-1a": "https://www.betclic.fr/football-s1/belgique-division-1a-c26",
			"super-lig": "https://www.betclic.fr/football-s1/turquie-super-lig-c37",
			"LDC":"https://www.betclic.fr/football-s1/ligue-des-champions-c8",
			"europa":"https://www.betclic.fr/football-s1/ligue-europa-c3453",
			"world":"https://www.betclic.fr/football-s1/qualif-europe-cdm-c2010",
			"all":"https://www.betclic.fr/football-s1",
		},
		# 'basketball':
		# {
		# 	"nba": "https://www.betclic.fr/basket-ball-s4/nba-c13",
		# 	"euroleague": "https://www.betclic.fr/basket-ball-s4/euroligue-c14",
		# }
}

filename='Team/TeamBetclic.txt'
tab=[]
pairs=[]
with open(filename,"r",encoding="utf8") as file:
    tab=file.read()
tab=tab.split(";\n")
for el in tab:
    el=el.split(",")
    pairs.append(el)


def get_page(competition):
	if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
		url = competition_urls[competition["sport"]][competition["competition"]]
	else:
		return None
	response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"})
	html = BeautifulSoup(response.content, 'html.parser')
	return html
	
def get_games(competition):

	html = get_page(competition)
	game=html.select(".cardEvent")

	games=[]
	nbr=0
	for el in game:
		team1="".join(el.select(".scoreboard_contestantLabel")[0].text.split())
		team2="".join(el.select(".scoreboard_contestantLabel")[1].text.split())

		odds_el=el.select(".market_odds")[0]
		odds=odds_el.select(".oddValue")
		oddf=[]
		for odd in odds:
			try :
				oddf.append(float("".join(odd.text.split()).replace(",", ".")))
			except:
				oddf.append(float(1))

		# with open("Team/Betclic.txt", 'a',encoding="utf-8") as file:
		# 	file.write(team1+"\n"+team2+"\n")

		for pair in pairs :
			if team1 == pair[0] and pair[1]!="":	
				team1=pair[1]
			if team2 == pair[0] and pair[1]!="":
				team2=pair[1]

		nbr=nbr+1
		games.append({
			'team1': team1,
			'team2': team2,
			'odds': oddf
		})
	print("Betclic = ",nbr)
	return games