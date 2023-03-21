# cloudbet.py

from os import replace, write
import requests
import json

competition_urls = {'football': {
    'ligue1': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-france-ligue-1/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'liga': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-spain-laliga/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'bundesliga': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-germany-bundesliga/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'premier-league': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-england-premier-league/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'serie-a': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-italy-serie-a/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'primeira': '',
    'serie-a-brasil': '',
    'a-league': '',
    'bundesliga-austria': '',
    'division-1a': '',
    'super-lig': '',
    'LDC': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-international-clubs-uefa-champions-league/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'europa': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-international-clubs-uefa-europa-league/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'world': 'https://www.cloudbet.com/sports-api/c/v6/sports/competitions/soccer-international-wc-qualification-uefa/events?markets=soccer.match_odds&markets=soccer.asian_handicap&markets=soccer.total_goals&locale=fr',
    'all': '',
    }, 'basketball': {'nba': '', 'euroleague': ''}}

filename = 'Team/TeamCloudOne.txt'
tab = []
pairs = []
with open(filename, 'r', encoding='utf8') as file:
    tab = file.read()
tab = tab.split(';\n')
for el in tab:
    el = el.split(',')
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
    'Cookie': 'lng=en; flaglng=en; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=BbblOWFXM1ESU8VHB/1dAg==; sh.session_be98639c=04c362af-da44-4e0e-a384-ca2529fa5712; SESSION=4d9c3757128519eb87309f34d670d560; visit=1-378d9869df866ea72e6818eb52cb9af1; coefview=0; blocks=1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; completed_user_settings=true; ggru=160; right_side=right; pushfree_status=canceled; _glhf=1633191759',
    }


def get_json(competition):

    if competition['sport'] in competition_urls \
        and competition['competition'] \
        in competition_urls[competition['sport']]:
        url = competition_urls[competition['sport'
                               ]][competition['competition']]
    else:
        return None
    r = requests.get(url, headers=headers)
    request = r.json()
    return request


def get_games(competition):
    json = get_json(competition)
    games = []
    nbr = 0

    for event in json['events']:

        team1 = event["home"]["name"]
        team2 = event["away"]["name"]

        odds=[
            float("{:.2f}".format(event["markets"]["soccer.match_odds"]["submarkets"]["period=ft"]["selections"][0]["price"])),
            float("{:.2f}".format(event["markets"]["soccer.match_odds"]["submarkets"]["period=ft"]["selections"][1]["price"])),
            float("{:.2f}".format(event["markets"]["soccer.match_odds"]["submarkets"]["period=ft"]["selections"][2]["price"])),
           ]
        

        for pair in pairs:
            if team1 == pair[0] and pair[1] != '':
                team1 = pair[1]
            if team2 == pair[0] and pair[1] != '':
                team2 = pair[1]
        nbr = nbr + 1

        # with open('Team/CloudOne.txt', 'a', encoding='utf-8') as file:
        #     file.write(team1 + '\n' + team2 + '\n')

        games.append({
            'team1': team1,
            'team2': team2,
            'odds': odds
        })

    print ('Cloudbet = ', nbr)
    return games