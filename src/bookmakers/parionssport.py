#!/usr/bin/python
# -*- coding: utf-8 -*-
# parionssport.py

import log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import traceback
import config

competition_urls = {'football': {
    'ligue1': 'https://www.enligne.parionssport.fdj.fr/paris-football/france/ligue-1-uber-eats',
    'liga': 'https://www.enligne.parionssport.fdj.fr/paris-football/espagne/liga-primera',
    'bundesliga': 'https://www.enligne.parionssport.fdj.fr/paris-football/allemagne/bundesliga-1',
    'premier-league': 'https://www.enligne.parionssport.fdj.fr/paris-football/angleterre/premier-league?filtre=58532401',
    'serie-a': 'https://www.enligne.parionssport.fdj.fr/paris-football/italie/serie-a',
    'primeira': '',
    'serie-a-brasil': '',
    'a-league': '',
    'bundesliga-austria': '',
    'division-1a': '',
    'super-lig': '',
    'LDC': 'https://www.enligne.parionssport.fdj.fr/paris-football/coupes-d-europe/championsleague?filtre=58532497',
    'europa': 'https://www.enligne.parionssport.fdj.fr/paris-football/coupes-d-europe/europa-league?filtre=58532492',
    'world': 'https://www.enligne.parionssport.fdj.fr/paris-football/international/cdm-q-europe?filtre=58566520',
    'all': 'https://www.enligne.parionssport.fdj.fr/paris-football',
    }}

        # 'basketball':
        # {
        # ...."nba": "https://www.betclic.fr/basket-ball-s4/nba-c13",
        # ...."euroleague": "https://www.betclic.fr/basket-ball-s4/euroligue-c14",
        # }

filename = 'Team/TeamParionssport.txt'
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
    try:
        wait(driver,15).until(EC.presence_of_element_located((By.ID,'popin_tc_privacy_button_3'))).click()
    except:
        log.log_Error('Error : During Parionssport scrapping --> Fail or No privacy pop up to close'
                      )
        pass

    games = wait(driver,
                 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                           'wpsel-bloc')))

    gamef = []
    nbr = 0
    for game in games:
        teams = wait(game,
                     15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                               'wpsel-desc')))
        for team in teams:
            try:
                team1 = ''.join(team.text.split('-')[0].split())
            except:
                team1 = 'fail'
            try:
                team2 = ''.join(team.text.split('-')[1].split())
            except:
                team2 = 'fail'

        odds = wait(game,
                    15).until(EC.presence_of_all_elements_located((By.CLASS_NAME,
                              'outcomeButton-data')))

        oddf = []
        if len(odds) == 3 and odds[0] != '' and odds[1] != '' \
            and odds[2] != '':
            for odd in odds:
                try:
                    oddf.append(float(odd.text.replace(',', '.')))
                except:
                    oddf.append(1)
        else:
            oddf = [1, 1, 1]

        for pair in pairs:
            try:
                if team1 == pair[0]:
                    team1 = pair[1]
                if team2 == pair[0]:
                    team2 = pair[1]
            except:
                pass

        # with open('Team/Parionssport.txt', 'a', encoding='utf-8') as \
        #     file:
        #     file.write(team1 + '\n' + team2 + '\n')

        nbr = nbr + 1
        gamef.append({'team1': team1, 'team2': team2, 'odds': oddf})

    # teams =driver.find_elements_by_class_name("wpsel-desc")
    # for team in teams:
    #     print (team.text)

    print ('Parionssport : ' + str(nbr))
    driver.quit()
    return gamef