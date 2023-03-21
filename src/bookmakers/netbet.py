from bs4 import BeautifulSoup
import requests
import datetime

competition_urls = {
	'football': 
	{
		"ligue1": "https://www.netbet.fr/football/france/ligue-1-uber-eats",
		"liga": "https://www.netbet.fr/football/espagne/laliga",
		"bundesliga": "https://www.netbet.fr/football/allemagne/bundesliga",
		"premier-league": "https://www.netbet.fr/football/angleterre/premier-league",
		"serie-a": "https://www.netbet.fr/football/italie/serie-a",
		"primeira": "https://www.netbet.fr/football/portugal/primeira-liga",
		"serie-a-brasil": "https://www.netbet.fr/football/bresil/brasileirao",
		"a-league": "https://www.netbet.fr/football/australie/a-league",
		"bundesliga-austria": "https://www.netbet.fr/football/autriche/bundesliga",
		"division-1a": "https://www.netbet.fr/football/belgique/pro-league",
		"super-lig": "https://www.netbet.fr/football/turquie/super-lig",
		"LDC":"https://www.netbet.fr/football/ligue-des-champions/ligue-des-champions",
		"europa":"https://www.netbet.fr/football/ligue-europa/ligue-europa",
		"world":"https://www.netbet.fr/football/coupe-du-monde",
		"all":"",
	},
	# 'basketball':
	# {
	# 	"nba": "https://www.netbet.fr/basketball/etats-unis/nba",
	# 	"euroleague": "https://www.netbet.fr/basketball/coupes-d-europe/euroligue",
	# }
}

filename='Team/TeamNetbet.txt'
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
	games = []
	game_elements = html.select(".nb-event")
	nbr=0
	for el in game_elements:
		names = el.select(".nb-match_actor")
		team1 = "".join(names[0].text.split())
		team2 = "".join(names[1].text.split())
		odd_els = el.select(".nb-odds_amount")
		odds = []
		for odd_el in odd_els[:3]:
			odds.append(float(odd_el.text.replace(",", ".")))
		
		if len(odds)<3:
			odds.append(float(1))

		# with open("Team/Netbet.txt", 'a',encoding="utf-8") as file:
		# 	file.write(team1+"\n"+team2+"\n")
		try :	
			date=el.select(".nb-event_datestart")[0].text
			if date=="Auj.":
				date=datetime.date.today()
			else:
				date=datetime.date(2021,int(date.split("/")[1]),int(date.split("/")[0]))
		except:
			date="/"
		
		for pair in pairs :
			if team1 == pair[0] and pair[1]!="":	
				team1=pair[1]
			if team2 == pair[0] and pair[1]!="":
				team2=pair[1]
		
		nbr=nbr+1
		games.append({
			'team1': team1,
			'team2': team2,
			'odds': odds,
			'date':date,
		})
	print("Netbet = ",nbr)
	return games