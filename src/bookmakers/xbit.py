# 1xbit.py

from os import replace, write
import requests
import json

competition_urls = {'football': {
    'ligue1': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=12821&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'liga': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=127733&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'bundesliga': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=96463&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'premier-league': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'serie-a': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=110163&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'primeira': '',
    'serie-a-brasil': '',
    'a-league': '',
    'bundesliga-austria': '',
    'division-1a': '',
    'super-lig': '',
    'LDC': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=118587&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'europa': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=118593&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'world': 'https://1xbit.com/LineFeed/Get1x2_VZip?sports=1&champs=2286681&count=50&lng=fr&tf=2200000&mode=4&country=198&partner=65&getEmpty=true',
    'all': '',
    }, 'basketball': {'nba': '', 'euroleague': ''}}

filename = 'Team/TeamBet22.txt'#meme api que bet22 et 1xbet
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

    for event in json['Value']:

        team1 = event["O1"]
        team2 = event["O2"]

        if team1=="à domicile (buts marqués)" or team2=="à l'extérieur (buts marqués)" or team2=="Away (Special bets)" or team1=="Equipe locale (paris spéciuax)":
            continue

        odds=[
            float("{:.2f}".format(event["E"][0]["C"])),
            float("{:.2f}".format(event["E"][1]["C"])),
            float("{:.2f}".format(event["E"][2]["C"])),
           ]
        

        for pair in pairs:
            if team1 == pair[0] and pair[1] != '':
                team1 = pair[1]
            if team2 == pair[0] and pair[1] != '':
                team2 = pair[1]
        nbr = nbr + 1

        # with open('Team/1xbit.txt', 'a', encoding='utf-8') as file:
        #     file.write(team1 + '\n' + team2 + '\n')

        games.append({
            'team1': team1,
            'team2': team2,
            'odds': odds
        })

    print ('Xbit = ', nbr)
    return games