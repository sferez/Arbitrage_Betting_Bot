from datetime import datetime
import os
import time
import sys
import config
import ssl
import requests
import glob
import twitterbot
import config
import traceback
ssl._create_default_https_context = ssl._create_unverified_context

Telegram_waiting_time = 1

def telegram_bot_sendtext(bot_message):
    
    bot_token = config.bot_token
    bot_chatID = config.bot_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

def telegram_bot_Error(bot_message):
    
    bot_token = config.botError_token
    bot_chatID = config.botError_chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

 

def init():
	global filename
	global filenamedata
	global filenameError
	global filenameFound
	global last_telegram_message
	last_telegram_message = time.time()
	filename = "./logs/{}.log".format(datetime.now().strftime("%d.%m.%Y_%H%M%S"))
	with open(filename, "w+") as _:
		pass
	filenamedata = "./Data/{}.log".format(datetime.now().strftime("%d.%m.%Y"))
	with open(filenamedata, "a+") as _:
		pass
	filenameError = "./Errors/{}.log".format(datetime.now().strftime("%d.%m.%Y"))
	with open(filenameError, "a+") as _:
		_.write(filename+"\n")
		pass
	filenameFound = "./Founds/{}.log".format(datetime.now().strftime("%d.%m.%Y"))
	with open(filenameFound, "a+") as _:
		pass
	twitterbot.init()

def log(message, end="\n"):
	with open(filename, 'a',encoding="utf-8") as file:
		file.write(message + end)

def telegram(message,profit):
	global last_telegram_message
	if profit<config.profittwitterz:
		try:
			twitterbot.twitter(message)
		except:
			log("Error : Cannot send message Twitter "+traceback.format_exc())
			log_Error("Error : Cannot send message Twitter ")
	else:
		try:
			twitterbot.twitterz(message)
		except:
			log("Error : Cannot send message Twitter Z "+traceback.format_exc())
			log_Error("Error : Cannot send message Twitter Z ")

	if profit >config.profittelegram:
		try:
			while (time.time() - last_telegram_message < Telegram_waiting_time):
				time.sleep(Telegram_waiting_time)
			last_telegram_message = time.time()
			telegram_bot_sendtext(message)
		except:
			log("Error: cannot send message on Telegram: "+traceback.format_exc())
			log_Error("Error : Cannot send message Telegram ")

	print(message)


def del_log() :
	
	paths = [
		r'./logs',
		# r'Founds',
		r'../Errors',
		# r"logs",
		# r"Errors",
	]
	for path in paths:
		today = datetime.today()#gets current time
		os.chdir(path) #changing path to current path(same as cd command)

		#we are taking current folder, directory and files 
		#separetly using os.walk function
		for root,directories,files in os.walk(path,topdown=False): 
			for name in files:
				#this is the last modified time
				t = os.stat(os.path.join(root, name))[8] 
				filetime = datetime.fromtimestamp(t) - today

				#checking if file is more than 7 days old 
				#or not if yes then remove them
				if filetime.days <= -7:
					print(os.path.join(root, name), filetime.days)
					os.remove(os.path.join(root, name))


def log_data(message, end="\n"):
	with open(filenamedata, 'a',encoding="utf-8") as file:
		file.write(message + end)

def log_Error(message, end="\n"):
	with open(filenameError, 'a',encoding="utf-8") as file:
		file.write(message + end)

def log_Found(message, end="\n"):
	with open(filenameFound, 'a',encoding="utf-8") as file:
		file.write(message + end)

