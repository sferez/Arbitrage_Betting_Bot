# Arbitrage Betting Bot

## Description

This is a arbitrage betting bot that scrap all the bookmakers and find the best arbitrage possible.

## Disclaimer

- Project date : 2019
- The project is not maintained and update since 2019
- This is a personal project for the purpose of learning Python. The code is not optimized and is not intended to be used in production.
- This is a personal project, I'm not responsible for any loss of money or any other problem that could occur with this bot.

## Report



## Sites scraped:
    
    FR :
        - Unibet
        - Winamax
        - Betclic
        - Zebet
        - Netbet
        - PMU
        - Parionssport

    World Wide :
        - Pinnacle
        - 1Xbet
        - 22 Bet
        - Marathon
        - XBit
        - Sportbet One
        - Stake
        - CloudBet

## Library use for scrapping:

    - Selenium : for dynamic site (Parionssport, Pinnacle, Unibet)
    - Bs4 : for static site (PMU, Betclic, Zebet, Netbet, Marathon)
    - Request : for download directly json file from site when possible (1Xbet, 22 Bet, Winamax)

## Logs:

    - Logs : full log in ./logs
    - Data : Only Data log in ./Data for IA analyze later
    - Founds : Log of the arbitrage found to not repeat the notification if it's already found last time
    - Errors : log of the errors that occured

## Style of arb:

    - only_best_arb : select the best odd in the list and only arb bewteen the best odd of team1, team2 and draw
    - all_posibility : test all the posibility of arb possible bewteen bookmakers

## Notification: 

    - Use of Telegram Bot channel for user's notifications
    - Use of Twitter account to post the arbitrage found via API

## Dependencies:

    - Selenium
    - bs4
    - requests
    - tweepy

## To run:

- must create /Data
- /Founds with a txt file in the directory
- /logs
- /Errors
- Config all the data in config.py
- have a chromedriver.exe and setup the path in config.py

## Authors

- [@sferez](https://github.com/sferez)