#Unibet.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import config


competition_urls = {
		'football':
		{
			"ligue1": "https://www.unibet.fr/sport/football/ligue-1-ubereats",
			"liga": "https://www.unibet.fr/sport/football/liga",
			"bundesliga": "https://www.unibet.fr/sport/football/bundesliga",
			"premier-league": "https://www.unibet.fr/sport/football/premier-league",
			"serie-a": "https://www.unibet.fr/sport/football/serie-a",
			"primeira": "",
			"serie-a-brasil": "",
			"a-league": "",
			"bundesliga-austria": "",
			"division-1a": "",
			"super-lig": "",
			"LDC":"https://www.unibet.fr/sport/football/ligue-des-champions",
			"europa":"https://www.unibet.fr/sport/football/europa-league",
			"world":"https://www.unibet.fr/sport/football/coupe-du-monde-qualifications",
			"all":"https://www.unibet.fr/sport/football",
		},
		# 'basketball':
		# {
		# 	"nba": "https://www.betclic.fr/basket-ball-s4/nba-c13",
		# 	"euroleague": "https://www.betclic.fr/basket-ball-s4/euroligue-c14",
		# }
}

filename='Team/TeamUnibet.txt'
tab=[]
pairs=[]
with open(filename,"r",encoding="utf8") as file:
    tab=file.read()
tab=tab.split(";\n")
for el in tab:
    el=el.split(",")
    pairs.append(el)


def get_url(competition):
	if (competition["sport"] in competition_urls and competition["competition"] in competition_urls[competition["sport"]]):
		url = competition_urls[competition["sport"]][competition["competition"]]
	else:
		return None
	return url

def get_games(competition):
    url = get_url(competition)

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--incognito")
    options.add_argument("--log-level=3")
    options.add_argument('--ignore-certificate-errors-spki-list')
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.headless = True

    DRIVER_PATH = config.path
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)

    games=wait(driver,15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"had-market")))
    gamef=[]
    nbr=0
    for i, game in enumerate(games):
        if i%2==0:
            # print(str(i)+"  "+str(game))
            teams=wait(game,15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"cell-event")))
            teams=teams[0].text.split("-")
            team1="".join(teams[0].split())
            team2="".join(teams[1].split())
        if i%2==1:
            # print(str(i)+"  "+str(game))
            odds=wait(game,15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"price")))
            odd1=float(odds[1].text)
            odd2=float(odds[3].text)
            odd3=float(odds[5].text)
            oddf=[
                odd1,
                odd2,
                odd3]
            
            # with open("Team/Unibet.txt", 'a',encoding="utf-8") as file:
            #     file.write(team1+"\n"+team2+"\n")

            for pair in pairs :
                try:
                    if team1 == pair[0]:	
                        team1=pair[1]
                    if team2 == pair[0]:
                        team2=pair[1]
                except:
                    pass

            gamef.append({
                "team1":team1,
                "team2":team2,
                "odds":oddf,
            })
            nbr=nbr+1
    print("Unibet : "+str(nbr))
    driver.quit()
    return gamef