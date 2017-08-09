import json
import urllib2
import numpy as np
import keys

API_ROOT_URL = r"https://na1.api.riotgames.com"
API_KEY = keys.API_KEY
CHAMP_DATA = r"/lol/static-data/v3/champions?locale=en_US&dataById=false&api_key="
MASTERY_DATA = r"/lol/champion-mastery/v3/champion-masteries/by-summoner/"
SUMM_BY_NAME = r"/lol/summoner/v3/summoners/by-name/"
exampleLog = "chimpnoises has joined the game\nsiiverfire has joined the game\nbrown hanky has joined the game\ncomesicle has joined the game\nunidenj has joined the game"

def getChampNames():
    try:
        champs = json.loads(urllib2.urlopen(CHAMP_DATA+API_KEY).read())
        return champs
    except urllib2.HTTPError as e:
        print e
        return []

def getPlayerNames(chatlog):
    names = []
    for i in chatlog.split('\n'):
        newname = i[:len(i)-20]
        newname = newname.replace(" ","%20")
        if len(names) < 5 and newname not in names:
            names.append(newname)
    return names

def getSummonerId(arr):
    nameDict = {}
    for i in arr:
        data = json.loads(urllib2.urlopen(API_ROOT_URL+SUMM_BY_NAME+i+r"?api_key="+API_KEY).read())
        nameDict[data["name"]] = data["id"]
    return nameDict

def getMasteryScores(dic):
    for key,val in dic.items():
        data = json.loads(urllib2.urlopen(API_ROOT_URL+MASTERY_DATA+str(val)+r"?api_key="+API_KEY).read())
        print key, data


#labels = getChampNames()
playerNames = getPlayerNames(exampleLog)
summId = getSummonerId(playerNames)
print summId
getMasteryScores(summId)
