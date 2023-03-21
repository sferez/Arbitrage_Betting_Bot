#1xbet.py
from os import replace, write
import requests
import json

competition_urls = {
	'football':
	{
		"ligue1": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=12821&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"liga": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"bundesliga": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"premier-league": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"serie-a": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"primeira": "",
		"serie-a-brasil": "",
		"a-league": "",
		"bundesliga-austria": "",
		"division-1a": "",
		"super-lig": "",
		"LDC": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=118587&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"europa": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=118593&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
		"world": "https://br.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=1&champs=2286681&count=20&lng=fr&tz=2&mode=4&country=31&partner=132&getEmpty=true&virtualSports=true",
	},
	
}

filename='Team/TeamBet22.txt'#fait expres Bet22 meme api que Xbet
tab=[]
pairs=[]
with open(filename,"r",encoding="utf8") as file:
    tab=file.read()
tab=tab.split(";\n")
for el in tab:
    el=el.split(",")
    pairs.append(el)

headers = {
  'Connection': 'keep-alive',
  'Accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'Sec-GPC': '1',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://1xbet.com/en/line/',
  'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cookie': 'lng=en; flaglng=en; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=BbblOWFXM1ESU8VHB/1dAg==; sh.session_be98639c=04c362af-da44-4e0e-a384-ca2529fa5712; SESSION=4d9c3757128519eb87309f34d670d560; visit=1-378d9869df866ea72e6818eb52cb9af1; coefview=0; blocks=1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; completed_user_settings=true; ggru=160; right_side=right; pushfree_status=canceled; _glhf=1633191759'
}

def get_json(competition):

	if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
		url = competition_urls[competition["sport"]][competition["competition"]]
	else:
		return None
	r = requests.get(url, headers=headers)
	request=r.json()
	return request



def get_games(competition):
	json = get_json(competition)
	games = []
	nbr=0

	for game in json['Value']:

		if game["O1"]=="Home (Goals)" or game["O2"]=="Away (Goals)" or game["O1"]=="Home (Special bets)" or game["O2"]=="Away (Special bets)" or game["O1"]=="à domicile (buts marqués)" or game["O2"]=="à l'extérieur (buts marqués)":
			continue

		odds = [
		game['E'][0]['C'],
    	game['E'][1]['C'],
    	game['E'][2]['C']
    	]
	    	
		for pair in pairs :
			if game["O1"] == pair[0] and pair[1]!="":	
				game["O1"]=pair[1]
			if game["O2"] == pair[0] and pair[1]!="":
				game["O2"]=pair[1]
		nbr=nbr+1

		# with open("Team/Xbet.txt", 'a',encoding="utf-8") as file:
		# 	file.write(game["O1"]+"\n"+game["O2"]+"\n")

		games.append({
			'team1': game["O1"],
			'team2': game["O2"],
			'odds': odds
		})
	print("xbet = ",nbr)	
	return games



