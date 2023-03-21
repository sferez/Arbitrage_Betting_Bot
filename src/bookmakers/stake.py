#stake.py
from bs4 import BeautifulSoup
import requests

competition_urls = {'football': {
    'ligue1': 'https://stake.com/sports/soccer/france/ligue-1',
    'liga': 'https://stake.com/sports/soccer/spain/la-liga',
    'bundesliga': 'https://stake.com/sports/soccer/germany/bundesliga',
    'premier-league': 'https://stake.com/sports/soccer/england/premier-league',
    'serie-a': 'https://stake.com/sports/soccer/italy/serie-a',
    'primeira': '',
    'serie-a-brasil': '',
    'a-league': '',
    'bundesliga-austria': '',
    'division-1a': '',
    'super-lig': '',
    'LDC': 'https://stake.com/sports/soccer/international-clubs/uefa-champions-league',
    'europa': 'https://stake.com/sports/soccer/international-clubs/uefa-europa-league',
    'world': 'https://stake.com/sports/soccer/international/wc-qualification-uefa',
    'all': '',
    }, 'basketball': {'nba': '', 'euroleague': ''}}

filename = 'Team/TeamStake.txt'
tab = []
pairs = []
with open(filename, 'r', encoding='utf8') as file:
    tab = file.read()
tab = tab.split(';\n')
for el in tab:
    el = el.split(',')
    pairs.append(el)


def get_page(competition):
    if competition['sport'] in competition_urls \
        and competition['competition'] \
        in competition_urls[competition['sport']]:
        url = competition_urls[competition['sport'
                               ]][competition['competition']]
    else:
        return None
    response = requests.get(url,
                            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
                            })
    html = BeautifulSoup(response.content, 'html.parser')
    return html


def get_games(competition):
    html = get_page(competition)
    games = []
    game_elements = html.select('.fixture-preview')
    nbr = 0
    for el in game_elements:
        names = el.select('.content-or-loader')
        team1 = ''.join(names[0].text.split())
        team2 = ''.join(names[1].text.split())
        odd_els = el.select('.odds')
        odds = []
        for odd_el in odd_els[::2]:
           odds.append(float(odd_el.text.replace(',', '.')))

        # with open('Team/Stake.txt', 'a', encoding='utf-8') as file:
        #     file.write(team1 + '\n' + team2 + '\n')

        for pair in pairs:
            if team1 == pair[0] and pair[1] != '':
                team1 = pair[1]
            if team2 == pair[0] and pair[1] != '':
                team2 = pair[1]

        nbr = nbr + 1
        games.append({'team1': team1, 'team2': team2, 'odds': odds})
    print ('Stake : ', nbr)
    return games
