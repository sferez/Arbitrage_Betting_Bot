# sportbetone.py

from os import replace, write
import requests
import json

competition_urls = {'football': {
    'ligue1': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96487},
    'liga': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96574},
    'serie-a': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96522},
    'LDC': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96684},
    'europa': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96683},
    'world': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":97184},
    'premier-league': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96482},
    'bundesliga': {"url":'https://api.sportbet.one/v1/events?sport=1&type=1',"code":96497},
    }}

filename = 'Team/TeamSportbetone.txt'
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
    r = requests.get(url["url"], headers=headers)
    request = r.json()
    return request


def get_games(competition):
    json = get_json(competition)
    code=competition_urls[competition['sport']][competition["competition"]]["code"]
    games = []
    nbr = 0

    for event in json['events']:
        if event["l"]!=code:
            continue

        team1 = event["h"]
        team2 = event["a"]

        odds=[
            event["o"]["1"]["h"],
            event["o"]["1"]["d"],
            event["o"]["1"]["a"],]
        

        for pair in pairs:
            if team1 == pair[0] and pair[1] != '':
                team1 = pair[1]
            if team2 == pair[0] and pair[1] != '':
                team2 = pair[1]
        nbr = nbr + 1

        # with open('Team/SportBetOne.txt', 'a', encoding='utf-8') as file:
        #     file.write(team1 + '\n' + team2 + '\n')

        games.append({
            'team1': team1,
            'team2': team2,
            'odds': odds
        })

    print ('SportBetOne = ', nbr)
    return games