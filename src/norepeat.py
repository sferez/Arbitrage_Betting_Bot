#norepeat
import glob
import os

def init():
    global seen
    seen = []
    directory = glob.glob('./Founds/*') 
    latest_file = max(directory, key=os.path.getctime)

    with open(latest_file, "r", encoding="utf-8") as file:
        content=file.read()
    content=content.split("\n")

    for found in content:
        if found!="":
            found=found.split(";")
            seen.append({
                "profit":float(found[0]),
                "team1":found[1],
                "team2":found[2],
                "book1":found[3],
                "book2":found[4],
                "book3":found[5],
                "odd1":float(found[6]),
                "odd2":float(found[7]),
                "odd3":float(found[8]),
            })

def check(profit,team1,team2,book1,book2,book3):
    for found in seen:
        if team1 == found["team1"] and team2 == found["team2"] and profit==found["profit"] and book1==found["book1"] and book2==found["book2"] and book3==found["book3"] :
            return True
    return False
    

