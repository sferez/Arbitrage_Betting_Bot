#marathon.py

from bs4 import BeautifulSoup
import requests

competition_urls = {
		'football':
		{
			"ligue1": "https://www.marathonbet.com/fr/popular/Football/France/Ligue+1+-+21533?interval=ALL_TIME",
			"liga": "https://www.marathonbet.com/fr/popular/Football/Spain/Primera+Division+-+8736?interval=ALL_TIME",
			"bundesliga": "https://www.marathonbet.com/fr/popular/Football/Germany/Bundesliga+-+22436?interval=ALL_TIME",
			"premier-league": "https://www.marathonbet.com/fr/popular/Football/England/Premier+League+-+21520?interval=ALL_TIME",
			"serie-a": "https://www.marathonbet.com/fr/popular/Football/Italy/Serie+A+-+22434?interval=ALL_TIME",
			"primeira": "",
			"serie-a-brasil": "",
			"a-league": "",
			"bundesliga-austria": "",
			"division-1a": "",
			"super-lig": "",
			"LDC":"https://www.marathonbet.com/fr/popular/Football/Clubs.+International/UEFA+Champions+League+-+21255?interval=ALL_TIME",
			"europa":"https://www.marathonbet.com/fr/popular/Football/Clubs.+International/UEFA+Europa+League+-+21366?interval=ALL_TIME",
			"world":"https://www.marathonbet.com/fr/popular/Football/Internationals+-+4410142?interval=ALL_TIME",
			"all":"https://www.marathonbet.com/fr/popular/Football+-+11?interval=ALL_TIME",
		},
		# 'basketball':
		# {
		# 	"nba": "https://www.betclic.fr/basket-ball-s4/nba-c13",
		# 	"euroleague": "https://www.betclic.fr/basket-ball-s4/euroligue-c14",
		# }
}

filename='Team/TeamMarathon.txt'
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
    html=get_page(competition)
    games=html.select(".sub-row")
    gamef=[]
    nbr=0

    for game in games:
        oddf=[]
        teams=game.select(".member-link")
        team1="".join(teams[0].text.split())
        team2="".join(teams[1].text.split())

        odds=game.select(".active-selection")
        for odd in odds:
            oddf.append(float(odd.text))

        for pair in pairs :
            try:
                if team1 == pair[0]:	
                    team1=pair[1]
                if team2 == pair[0]:
                    team2=pair[1]
            except:
                pass

        # with open("Team/Marathon.txt", 'a',encoding="utf-8") as file:
        #     file.write(team1+"\n"+team2+"\n")
        
        nbr=nbr+1
        gamef.append({
            "team1":team1,
            "team2":team2,
            "odds":oddf,
        })
    print("marathon = "+str(nbr))
    return gamef

