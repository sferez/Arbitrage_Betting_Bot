#Config file

# Select style of arbitrage :
styleArb="only_best_arb"
# styleArb="all_possibility"

# Chromedriver Path :
# path=r"/usr/bin/chromedriver"
path=r"C:\Windows\chromedriver.exe"

#Select the level you want to received profit notification
profitnotification=0.25
#min for twitterz
profittwitterz=1.25
#min for telegram
profittelegram=1

# Telegram Bot credential :
bot_token = ''
bot_chatID = ''

# Telegram Error bot credential
botError_token=""
botError_chatID=""

# twitter Bot credential :
consumer_key=""
consumer_secret=""
acces_token=""
acces_token_secret=""

hashtag="\n#football #sport #betting #bot"

consumer_keyz=""
consumer_secretz=""
acces_tokenz=""
acces_token_secretz=""

#Comment or uncomment the competition you want to analyze
competitions = [
	{'sport': "football", 'competition': "ligue1"},
	{'sport': "football", 'competition': "liga"},
	{'sport': "football", 'competition': "LDC"},
	{'sport': "football", 'competition': "europa"},
	# {'sport': "football", 'competition': "world"},
	{'sport': "football", 'competition': "bundesliga"},
	{'sport': "football", 'competition': "premier-league"},
	{'sport': "football", 'competition': "serie-a"},
#	{'sport': "football", 'competition': "primeira"},
#	{'sport': "football", 'competition': "serie-a-brasil"},
#	{'sport': "football", 'competition': "a-league"},
#	{'sport': "football", 'competition': "bundesliga-austria"},
#	{'sport': "football", 'competition': "division-1a"},
#	{'sport': "football", 'competition': "super-lig"},
	# {'sport': "basketball", "competition": "nba"},
#	{'sport': "basketball", "competition": "euroleague"},
]
