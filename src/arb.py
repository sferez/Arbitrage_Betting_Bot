import datetime
from difflib import SequenceMatcher
import log
import norepeat
import config

def str_similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()

def get_game(game, others):
	if (len(others) == 0 or game == None):
		return None
	m = 0
	m_obj = None
	for other in others:
		sim = str_similarity(game['team1'], other['team1']) + str_similarity(game['team2'], other['team2'])
		if (sim > m):
			m = sim
			m_obj = other
	if (str_similarity(game['team1'], m_obj['team1']) < 0.81):
		return None
	if (str_similarity(game['team2'], m_obj['team2']) < 0.81):
		return None
	return m_obj

def arb3(a, n, b):
	return (1 - (1/a + 1/n + 1/b)) * 100

def arb2(a, b):
	return (1 - (1/a + 1/b)) * 100

def dec_to_base(num, base):
	base_num = ""
	while (num > 0):
		dig = int(num % base)
		if (dig < 10):
			base_num += str(dig)
		else:
			base_num += chr(ord('A')+dig-10)
		num //= base
	base_num = base_num[::-1]
	return base_num

def arb_football(games):
	styleArb=config.styleArb
	nb_bookmakers = len(games)
	combinations = nb_bookmakers ** 3
	log.log("-- Arbitrage on: ")
	profitnotification=config.profitnotification
	for game in games:
		log.log("{:10}: {} - {} @{}/{}/{}".format(game, games[game]['team1'], games[game]['team2'], games[game]['odds'][0], games[game]['odds'][1], games[game]['odds'][2]))
	
	if styleArb=="only_best_arb":
		t1,t2,draw=0,0,0
		for i,game in enumerate(games):
			if games[game]['odds'][0]>t1:
				t1=games[game]['odds'][0]
				b1=list(games.keys())[int(i)]
			if games[game]['odds'][2]>t2:
				t2=games[game]['odds'][2]
				b3=list(games.keys())[int(i)]
			if games[game]['odds'][1]>draw:
				draw=games[game]['odds'][1]
				b2=list(games.keys())[int(i)]
		cotesmax="Best Odds : Team 1 = "+str(t1)+" ; Draw = "+str(draw)+" ; Team 2 = "+str(t2)
		books="Books = "+str(b1)+" ; "+str(b2)+" ; "+str(b3)
		log.log(cotesmax)
		log.log(books)
		profit = arb3(t1,draw,t2)
		

		if (profit > 0):
			try:
				date=games["netbet"]["date"]
				date=date-datetime.date.today()
				date=str(date).split(" ")[0]
			except:
				date="/"
				pass
			if norepeat.check(float("{:.2f}".format(profit)),games[b1]['team1'],games[b1]['team2'],b1,b2,b3)==False:
				if profit <0.5:
					gain="Small"
				elif profit <1.5:
					gain="Medium"
				else :
					gain="Huge"
				log.log("FOUND!!!!")
				stakes = get_stakes3(
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
					1000)
				if date!="/":
					score=(profit/float(date))*10
				else:
					score = 0
				if profit >profitnotification:	
					log.telegram("/!\Arbitrage Found/!\ \n- Profit = {:.2f}% ({}) \n- Match = {} vs {}\n- Books = {}/{}/{}\n- Odds = {} | {} | {}\n- Stakes[1000$] = {}$ | {}$ | {}$\n- Delay = {} Days\n- Score = {:.1f}".format(
						profit,
						gain,
						games[b1]['team1'],
						games[b1]['team2'],
						b1,
						b2,
						b3,
						games[b1]['odds'][0],
						games[b2]['odds'][1],
						games[b3]['odds'][2],
						stakes['rounded'][0],
						stakes['rounded'][1],
						stakes['rounded'][2],
						date,
						score
					),profit)
				log.log_Found("{:.2f};{};{};{};{};{};{};{};{};{};{:.1f}".format(
					profit,
					games[b1]['team1'],
					games[b1]['team2'],
					b1,
					b2,
					b3,
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
					date,
					score,
				))
			else:
				log.log("ALREADY FOUND LAST TIME SO NO NOTIFICATION !!!!")
				print("FOUND LAST TIME")
				stakes = get_stakes3(
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
					1000)
			
				
		log.log("({:10}/{:10}/{:10}) {:.2f}%".format(b1,b2,b3,profit))
	
	else :
		log.log("{} combinations possible --".format(combinations))		
		for i in range(combinations):
			combination = str(dec_to_base(i, nb_bookmakers)).zfill(3)
			comb=[]
			if combination[0]=="A":
				comb.append(10)
			else:
				comb.append(combination[0])
			if combination[1]=="A":
				comb.append(10)
			else:
				comb.append(combination[1])
			if combination[2]=="A":
				comb.append(10)
			else:
				comb.append(combination[2])
			if combination[0]=="B":
				comb.append(11)
			else:
				comb.append(combination[0])
			if combination[1]=="B":
				comb.append(11)
			else:
				comb.append(combination[1])
			if combination[2]=="B":
				comb.append(11)
			else:
				comb.append(combination[2])
			if combination[0]=="C":
				comb.append(12)
			else:
				comb.append(combination[0])
			if combination[1]=="C":
				comb.append(12)
			else:
				comb.append(combination[1])
			if combination[2]=="C":
				comb.append(12)
			else:
				comb.append(combination[2])		
			b1 = list(games.keys())[int(comb[0])]
			b2 = list(games.keys())[int(comb[1])]
			b3 = list(games.keys())[int(comb[2])]
			profit = arb3(
					games[b1]['odds'][0],
					games[b2]['odds'][1],
					games[b3]['odds'][2],
			)

			if (profit > 0):
				try:
					date=games["netbet"]["date"]
					date=date-datetime.date.today()
					date=str(date).split(" ")[0]
				except:
					date="/"
					pass
				if norepeat.check(float("{:.2f}".format(profit)),games[b1]['team1'],games[b1]['team2'],b1,b2,b3)==False:
					if profit <0.5:
						gain="Small"
					elif profit <1.5:
						gain="Medium"
					else :
						gain="Huge"
					log.log("FOUND!!!!")
					stakes = get_stakes3(
						games[b1]['odds'][0],
						games[b2]['odds'][1],
						games[b3]['odds'][2],
						1000)
					score=(profit/float(date))*10
					if profit > profitnotification:
						log.telegram("/!\Arbitrage Found/!\ \n- Profit = {:.2f}% ({}) \n- Match = {} vs {}\n- Books = {}/{}/{}\n- Odds = {} | {} | {}\n- Stakes[1000$] = {}$ | {}$ | {}$\n- Date = {} Days\n- Score = {:.1f}".format(
							profit,
							gain,
							games[b1]['team1'],
							games[b1]['team2'],
							b1,
							b2,
							b3,
							games[b1]['odds'][0],
							games[b2]['odds'][1],
							games[b3]['odds'][2],
							stakes['rounded'][0],
							stakes['rounded'][1],
							stakes['rounded'][2],
							date,
							score
						), profit)
					log.log_Found("{:.2f};{};{};{};{};{};{};{};{};{}:{:.1f}".format(
						profit,
						games[b1]['team1'],
						games[b1]['team2'],
						b1,
						b2,
						b3,
						games[b1]['odds'][0],
						games[b2]['odds'][1],
						games[b3]['odds'][2],
						date,
						score,
					))
				else:
					log.log("ALREADY FOUND LAST TIME SO NO NOTIFICATION !!!!")
					print("FOUND LAST TIME")
					stakes = get_stakes3(
						games[b1]['odds'][0],
						games[b2]['odds'][1],
						games[b3]['odds'][2],
						1000)
				
					
			log.log("{}: ({:10}/{:10}/{:10}) {:.2f}%".format(
				" ".join(combination.split()),
				b1,
				b2,
				b3,
				profit
			))

def arb_basketball(games):
	nb_bookmakers = len(games)
	combinations = nb_bookmakers ** 2
	log.log("-- Arbitrage on: ")
	for game in games:
		log.log("{:10}: {} - {} @{}/{}".format(game, games[game]['team1'], games[game]['team2'], games[game]['odds'][0], games[game]['odds'][1]))
	log.log("{} combinations possible --".format(combinations))
	for i in range(combinations):
		combination = str(dec_to_base(i, nb_bookmakers)).zfill(2)
		b1 = list(games.keys())[int(combination[0])]
		b2 = list(games.keys())[int(combination[1])]
		profit = arb2(
				games[b1]['odds'][0],
				games[b2]['odds'][1],
		)
		if (profit > 0):
			log.log("FOUND!!!!")
			stakes = get_stakes2(
				games[b1]['odds'][0],
				games[b2]['odds'][1],
				10)
			log.telegram("Abritrage found for **{}**-**{}** with **{}/{}** with odds {}/{}: {:.2f}%".format(
				games[b1]['team1'],
				games[b1]['team2'],
				b1,
				b2,
				games[b1]['odds'][0],
				games[b2]['odds'][1],
				profit
			))
			log.telegram("> Stakes: **{}**@{} on {} for A, **{}**@{} on {} for B".format(
				stakes['rounded'][0],
				games[b1]['odds'][0],
				b1,
				stakes['rounded'][1],
				games[b2]['odds'][1],
				b2
			))
		log.log("{}: ({:10}/{:10}) {:.2f}%".format(
			" ".join(combination.split()),
			b1,
			b2,
			profit
		))

def get_stakes3(a, n, b, investment):
	amount = arb3(a, n, b)
	tmp = (100 - amount) / 100
	return {
		'raw': (
			investment / (tmp * a),
			investment / (tmp * n),
			investment / (tmp * b)
		),
		'rounded': (
			round(investment / (tmp * a) * 10) / 10,
			round(investment / (tmp * n) * 10) / 10,
			round(investment / (tmp * b) * 10) / 10
		)
	}

def get_stakes2(a, b, investment):
	amount = arb2(a, b)
	tmp = (100 - amount) / 100
	return {
		'raw': (
			investment / (tmp * a),
			investment / (tmp * b)
		),
		'rounded': (
			round(investment / (tmp * a) * 10) / 10,
			round(investment / (tmp * b) * 10) / 10
		)
	}