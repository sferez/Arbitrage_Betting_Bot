import bookmakers.winamax as winamax
import bookmakers.pmu as pmu
import bookmakers.betclic as betclic
import bookmakers.zebet as zebet
import bookmakers.netbet as netbet
import bookmakers.xbet as xbet
import bookmakers.bet22 as bet22
import bookmakers.parionssport as parionssport
import bookmakers.pinnacle as pinnacle
import bookmakers.marathon as marathon
import bookmakers.unibet as unibet
import bookmakers.sportbetone as sbo
import bookmakers.stake as stake
import bookmakers.cloudbet as cloudbet
import bookmakers.xbit as xbit
import arb
import sys
import log
import config
import traceback
import time
import norepeat
from datetime import datetime


norepeat.init()
log.init()
log.telegram_bot_Error("Begin : "+datetime.now().strftime("%d.%m.%Y_%H%M%S"))
start=time.time()
progress = 0
for competition in config.competitions:
	print(competition["sport"]+" | "+competition["competition"])
	progress += 1
	bookmakers = {}
	booktocrawl="winamax"
	log.log_data(competition["sport"]+" | "+competition["competition"])
	try:
		bookmakers['winamax'] = winamax.get_games(competition)
		log.log("winamax: " + str(bookmakers['winamax']))
		log.log_data("winamax: " + str(bookmakers['winamax']))
	except:
		log.log("Cannot crawl winamax: " + traceback.format_exc())
		log.log_Error("Cannot crawl winamax: " + traceback.format_exc())
		booktocrawl='pmu'
	try:
		bookmakers['pmu'] = pmu.get_games(competition)
		log.log("pmu: " + str(bookmakers['pmu']))
		log.log_data("pmu: " + str(bookmakers['pmu']))
	except:
		log.log("Cannot crawl pmu: " + traceback.format_exc())
		log.log_Error("Cannot crawl pmu: " + traceback.format_exc())
		booktocrawl='betclic'
	try:
		bookmakers['betclic'] = betclic.get_games(competition)
		log.log("betclic: " + str(bookmakers['betclic']))
		log.log_data("betclic: " + str(bookmakers['betclic']))
	except:
		log.log("Cannot crawl betclic: " + traceback.format_exc())
		log.log_Error("Cannot crawl betclic: " + traceback.format_exc())
		booktocrawl='zebet'
	try:
		bookmakers['zebet'] = zebet.get_games(competition)
		log.log("zebet: " + str(bookmakers['zebet']))
		log.log_data("zebet: " + str(bookmakers['zebet']))
	except:
		log.log("Cannot crawl zebet: " + traceback.format_exc())
		log.log_Error("Cannot crawl zebet: " + traceback.format_exc())
		booktocrawl='netbet'
	try:
		bookmakers['netbet'] = netbet.get_games(competition)
		log.log("netbet: " + str(bookmakers['netbet']))
		log.log_data("netbet: " + str(bookmakers['netbet']))
	except:
		log.log("Cannot crawl netbet: " + traceback.format_exc())
		log.log_Error("Cannot crawl netbet: " + traceback.format_exc())
		booktocrawl='xbet'
	try:
		bookmakers['xbet'] = xbet.get_games(competition)
		log.log("xbet: " + str(bookmakers['xbet']))
		log.log_data("xbet: " + str(bookmakers['xbet']))
	except:
		log.log("Cannot crawl xbet: " + traceback.format_exc())
		log.log_Error("Cannot crawl xbet: " + traceback.format_exc())
		booktocrawl="bet22"
	try:
		bookmakers['bet22'] = bet22.get_games(competition)
		log.log("bet22: " + str(bookmakers['bet22']))
		log.log_data("bet22: " + str(bookmakers['bet22']))
	except:
		log.log("Cannot crawl bet22: " + traceback.format_exc())
		log.log_Error("Cannot crawl bet22: " + traceback.format_exc())
		booktocrawl='parionssport'
	try:
		bookmakers['parionssport'] = parionssport.get_games(competition)
		log.log("parionssport: " + str(bookmakers['parionssport']))
		log.log_data("parionssport: " + str(bookmakers['parionssport']))
	except:
		log.log("Cannot crawl Parionssport: " + traceback.format_exc())
		log.log_Error("Cannot crawl Parionssport: " + traceback.format_exc())
		booktocrawl='pinnacle'
	try:
		bookmakers['pinnacle'] = pinnacle.get_games(competition)
		log.log("pinnacle: " + str(bookmakers['pinnacle']))
		log.log_data("pinnacle: " + str(bookmakers['pinnacle']))
	except:
		log.log("Cannot crawl pinnacle: " + traceback.format_exc())
		log.log_Error("Cannot crawl pinnacle: " + traceback.format_exc())
		booktocrawl='marathon'
	try:
		bookmakers['marathon'] = marathon.get_games(competition)
		log.log("marathon: " + str(bookmakers['marathon']))
		log.log_data("marathon: " + str(bookmakers['marathon']))
	except:
		log.log("Cannot crawl marathon: " + traceback.format_exc())
		log.log_Error("Cannot crawl marathon: " + traceback.format_exc())
		booktocrawl='unibet'
	try:
		bookmakers['unibet'] = unibet.get_games(competition)
		log.log("unibet: " + str(bookmakers['unibet']))
		log.log_data("unibet: " + str(bookmakers['unibet']))
	except:
		log.log("Cannot crawl unibet: " + traceback.format_exc())
		log.log_Error("Cannot crawl unibet: " + traceback.format_exc())
		booktocrawl='sportbetone'
	try:
		bookmakers['sportbetone'] = sbo.get_games(competition)
		log.log("sportbetone: " + str(bookmakers['sportbetone']))
		log.log_data("sportbetone: " + str(bookmakers['sportbetone']))
	except:
		log.log("Cannot crawl sportbetone: " + traceback.format_exc())
		log.log_Error("Cannot crawl sportbetone: " + traceback.format_exc())
		booktocrawl='stake'
	try:
		bookmakers['stake'] = stake.get_games(competition)
		log.log("stake: " + str(bookmakers['stake']))
		log.log_data("stake: " + str(bookmakers['stake']))
	except:
		log.log("Cannot crawl stake: " + traceback.format_exc())
		log.log_Error("Cannot crawl stake: " + traceback.format_exc())
		booktocrawl='cloudbet'
	try:
		bookmakers['cloudbet'] = cloudbet.get_games(competition)
		log.log("cloudbet: " + str(bookmakers['cloudbet']))
		log.log_data("cloudbet: " + str(bookmakers['cloudbet']))
	except:
		log.log("Cannot crawl cloudbet: " + traceback.format_exc())
		log.log_Error("Cannot crawl cloudbet: " + traceback.format_exc())
		booktocrawl='xbit'
	try:
		bookmakers['xbit'] = xbit.get_games(competition)
		log.log("xbit: " + str(bookmakers['xbit']))
		log.log_data("xbit: " + str(bookmakers['xbit']))
	except:
		log.log("Cannot crawl xbit: " + traceback.format_exc())
		log.log_Error("Cannot crawl xbit: " + traceback.format_exc())
		booktocrawl='marathon'
	

	for game in bookmakers[booktocrawl]:
		games = {}
		for bookmaker in bookmakers:
			try:
				g = arb.get_game(game, bookmakers[bookmaker])
				if (g):
					games[bookmaker] = g
			except:
				log.log("Error while retrieving games: {}".format(traceback.format_exc()))
				log.log_Error("Error while retrieving games: {}".format(traceback.format_exc()))
		if (competition["sport"] == "football"):
			try:
				arb.arb_football(games)
			except:
				log.log("Error : Fail to arb (might be index out of range in odds[]" + traceback.format_exc())
				log.log_Error("Error : Fail to arb (might be index out of range in odds[]" + traceback.format_exc())
		# if (competition["sport"] == "basketball"):
		# 	arb.arb_basketball(games)
	print("Progess: {:.2f}%".format(progress / len(config.competitions) * 100))
	try:
		errorlog=competition["competition"]+";w="+str(len(bookmakers["winamax"]))+";z="+str(len(bookmakers["zebet"]))+";n="+str(len(bookmakers["netbet"]))+";u="+str(len(bookmakers["unibet"]))+";b="+str(len(bookmakers["betclic"]))+";pa="+str(len(bookmakers["parionssport"]))+";pm="+str(len(bookmakers["pmu"]))+";pi="+str(len(bookmakers["pinnacle"]))+";x="+str(len(bookmakers["xbet"]))+";m="+str(len(bookmakers["marathon"]))+";b2="+str(len(bookmakers["bet22"]))+";Xi="+str(len(bookmakers["xbit"]))+";cb="+str(len(bookmakers["cloudbet"]))+";sbo="+str(len(bookmakers["sportbetone"]))+";stk="+str(len(bookmakers["stake"]))
		log.telegram_bot_Error(errorlog)
	except:
		log.telegram_bot_Error("Error : fail to send logError Telegram")
		log.log_Error("Error : fail to send logError Telegram")
		pass

times=time.time()-start
print("End : time ="+str(times)+"s")
log.log("End : time ="+str(times)+"s")
log.telegram_bot_Error("End : time ="+str(times)+"s")
log.del_log()
