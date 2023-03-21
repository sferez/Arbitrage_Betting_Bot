import requests
import json
import log
import traceback

competition_urls = {
	'football':
	{
		"ligue1": "https://www.winamax.fr/paris-sportifs/sports/1/7/4",
		"liga": "https://www.winamax.fr/paris-sportifs/sports/1/32/36",
		"bundesliga": "https://www.winamax.fr/paris-sportifs/sports/1/30/42",
		"premier-league": "https://www.winamax.fr/paris-sportifs/sports/1/1/1",
		"serie-a": "https://www.winamax.fr/paris-sportifs/sports/1/31/33",
		"primeira": "https://www.winamax.fr/paris-sportifs/sports/1/44/52",
		"serie-a-brasil": "https://www.winamax.fr/paris-sportifs/sports/1/13/83",
		"a-league": "https://www.winamax.fr/paris-sportifs/sports/1/34/144",
		"bundesliga-austria": "https://www.winamax.fr/paris-sportifs/sports/1/17/29",
		"division-1a": "https://www.winamax.fr/paris-sportifs/sports/1/33/38",
		"super-lig": "https://www.winamax.fr/paris-sportifs/sports/1/46/62",
		"LDC":"https://www.winamax.fr/paris-sportifs/sports/1/800000542/23",
		"europa":"https://www.winamax.fr/paris-sportifs/sports/1/800000542/10909",
		"world":"https://www.winamax.fr/paris-sportifs/sports/1/4/900002365",
		"all":"https://www.winamax.fr/paris-sportifs/sports/1",
	},
	'basketball':
	{
		"nba": "https://www.winamax.fr/paris-sportifs/sports/2/800000076/177",
		"euroleague": "https://www.winamax.fr/paris-sportifs/sports/2/800000034/153",
	}
}

filename='Team/TeamWinamax.txt'
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
	html = response.text
	return html

def get_json(competition):
	html = get_page(competition)
	split1 = html.split("var PRELOADED_STATE = ")[1]
	split2 = split1.split(";</script>")[0]
	return json.loads(split2)

def get_id(competition):
	url = competition_urls[competition["sport"]][competition["competition"]]
	return int(url.split("/")[-1])

def get_games(competition):
	games = []
	json = get_json(competition)
	nbr=0
	for game in json['matches']:
		if (json['matches'][game]['tournamentId'] != get_id(competition)):
			continue
		try:
			team1 = "".join(json['matches'][game]['competitor1Name'].split())
		except:
			team1="fail"
		try:
			team2 = "".join(json['matches'][game]['competitor2Name'].split())
		except:
			team2="fail"
		bet_id = json['matches'][game]['mainBetId']
		bet = json['bets'][str(bet_id)]['outcomes']
		if (competition["sport"] == "football" and len(bet) != 3):
			continue
		if (competition["competition"] == "basketball" and len(bet) != 2):
			continue
		if (competition["sport"] == "football"):
			odds = [
				json['odds'][str(bet[0])],
				json['odds'][str(bet[1])],
				json['odds'][str(bet[2])],
			]
		elif (competition["sport"] == "basketball"):
			odds = [
				json['odds'][str(bet[0])],
				json['odds'][str(bet[1])],
			]
		
		# with open("Team/Winamax.txt", 'a',encoding="utf-8") as file:
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
			'odds': odds
		})
	print("Winamax = ",nbr)
	return games