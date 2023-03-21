#!/usr/bin/python
# -*- coding: utf-8 -*-
# pynnacle.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import log
import traceback
import config

competition_urls = {'football': {
    'ligue1': 'https://www.pinnacle.com/fr/soccer/france-ligue-1/matchups#period:0',
    'liga': 'https://www.pinnacle.com/fr/soccer/spain-la-liga/matchups#period:0',
    'bundesliga': 'https://www.pinnacle.com/fr/soccer/germany-bundesliga/matchups#period:0',
    'premier-league': 'https://www.pinnacle.com/fr/soccer/england-premier-league/matchups#period:0',
    'serie-a': 'https://www.pinnacle.com/fr/soccer/italy-serie-a/matchups#period:0',
    'primeira': '',
    'serie-a-brasil': '',
    'a-league': '',
    'bundesliga-austria': '',
    'division-1a': '',
    'super-lig': '',
    'LDC': 'https://www.pinnacle.com/fr/soccer/uefa-champions-league/matchups#period:0',
    'europa': 'https://www.pinnacle.com/fr/soccer/uefa-europa-league/matchups#period:0',
    'world': 'https://www.pinnacle.com/fr/soccer/fifa-world-cup-qualifiers-europe/matchups#period:0',
    'all': 'https://www.pinnacle.com/fr/soccer/matchups/highlights',
    }}

        # 'basketball':
        # {
        # ...."nba": "https://www.betclic.fr/basket-ball-s4/nba-c13",
        # ...."euroleague": "https://www.betclic.fr/basket-ball-s4/euroligue-c14",
        # }

filename = 'Team/TeamPinnacle.txt'
tab = []
pairs = []
with open(filename, 'r', encoding='utf8') as file:
    tab = file.read()
tab = tab.split(';\n')
for el in tab:
    el = el.split(',')
    pairs.append(el)


def get_url(competition):
    if competition['sport'] in competition_urls \
        and competition['competition'] \
        in competition_urls[competition['sport']]:
        url = competition_urls[competition['sport'
                               ]][competition['competition']]
    else:
        return None
    return url


def get_games(competition):

    url = get_url(competition)

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-blink-features=AutomationControlled'
                         )
    options.add_argument('--incognito')
    options.add_argument('--log-level=3')
    options.add_argument('--ignore-certificate-errors-spki-list')
    prefs = {'profile.managed_default_content_settings.images': 2}
    options.add_experimental_option('prefs', prefs)
    options.headless = True

    DRIVER_PATH = config.path
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,
                              options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)

    # try:
    # ....driver.find_element_by_id("popin_tc_privacy_button_2").click()
    # except:
    # ....pass

    games = wait(driver,
                 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                           'style_row__3hCMX')))
    gamef = []
    nbr = 0
    for game in games:
        teams = wait(game,
                     15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                               'style_participant__H8-ku')))

        try:
            team1 = ''.join(teams[0].text.split())
        except:
            team1 = 'fail'
            log.log_Error('Error Pinnacle scrapping during team asssigment : '
                           + traceback.format_exc())
        try:
            team2 = ''.join(teams[1].text.split())
        except:
            log.log_Error('Error Pinnacle scrapping during team asssigment : '
                           + traceback.format_exc())
            team2 = 'fail'

        odds = wait(game,
                    15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                              'style_price__15SlF')))
        oddf = []

        for odd in odds[:3]:
            try:
                oddf.append(float(odd.text))
            except:
                log.log_Error('Error Pinnacle scrapping during odds asssigment : '
                               + traceback.format_exc())
                oddf.append(1)

        for pair in pairs:
            try:
                if team1 == pair[0]:
                    team1 = pair[1]
                if team2 == pair[0]:
                    team2 = pair[1]
            except:
                pass

        # with open('Team/Pinnacle.txt', 'a', encoding='utf-8') as file:
        #     file.write(team1 + '\n' + team2 + '\n')

        nbr = nbr + 1
        gamef.append({'team1': team1, 'team2': team2, 'odds': oddf})

    # teams =driver.find_elements_by_class_name("wpsel-desc")
    # for team in teams:
    #     print (team.text)

    print ('Pinnacle : ' + str(nbr))
    driver.quit()
    return gamef
