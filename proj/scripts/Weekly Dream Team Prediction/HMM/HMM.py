# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:01:13 2017

@author: radha
"""

import csv
import numpy as np
import pandas as pd
from operator import itemgetter
from scipy.sparse import csr_matrix

data = pd.read_csv("FPL16.csv")
data = np.array(data)

playerDict = {}
for record in data:
    if (str(record[1])+record[2] not in playerDict):
        playerDict[str(record[1])+record[2]] = {}
    playerDict[str(record[1])+record[2]][record[45]] = {}
    playerDict[str(record[1])+record[2]][record[45]]['DreamTeam'] = record[39]
    playerDict[str(record[1])+record[2]][record[45]]['RoundPoints'] = record[6]

CountOne = 0
CountZero = 0
pointsOneLessTen = 0
pointsOneLessFive = 0
pointsZeroLessTen = 0
transitionZeroOne = 0
transitionOneZero = 0
pointsZeroLessFive = 0
pointsOneLessFifteen = 0
pointsZeroLessFifteen = 0
pointsOneGreaterFifteen = 0
pointsZeroGreaterFifteen = 0

for player in playerDict:
    weeks = list(reversed(sorted(playerDict[player].keys())))
    for week in weeks:
        if (week-1 in playerDict[player]):
            playerDict[player][week]['DreamTeam'] = playerDict[player][week]['DreamTeam'] - playerDict[player][week-1]['DreamTeam']
            if (playerDict[player][week]['DreamTeam'] == 0):
                CountZero = CountZero + 1
                if (playerDict[player][week-1]['DreamTeam'] == 1):
                    transitionOneZero = transitionOneZero + 1
                if (playerDict[player][week]['RoundPoints'] < 5):
                    pointsZeroLessFive = pointsZeroLessFive + 1
                    playerDict[player][week]['BjkIndex'] = 0
                elif (playerDict[player][week]['RoundPoints'] < 10):
                    pointsZeroLessTen = pointsZeroLessTen + 1
                    playerDict[player][week]['BjkIndex'] = 1
                elif (playerDict[player][week]['RoundPoints'] < 15):
                    pointsZeroLessFifteen = pointsZeroLessFifteen + 1
                    playerDict[player][week]['BjkIndex'] = 2
                else:
                    pointsZeroGreaterFifteen = pointsZeroGreaterFifteen + 1
                    playerDict[player][week]['BjkIndex'] = 3
            else:
                CountOne = CountOne + 1
                if (playerDict[player][week-1]['DreamTeam'] == 0):
                    transitionZeroOne = transitionZeroOne + 1
                if (playerDict[player][week]['RoundPoints'] < 5):
                    pointsOneLessFive = pointsOneLessFive + 1
                    playerDict[player][week]['BjkIndex'] = 0
                elif (playerDict[player][week]['RoundPoints'] < 10):
                    pointsOneLessTen = pointsOneLessTen + 1
                    playerDict[player][week]['BjkIndex'] = 1
                elif (playerDict[player][week]['RoundPoints'] < 15):
                    pointsOneLessFifteen = pointsOneLessFifteen + 1
                    playerDict[player][week]['BjkIndex'] = 2
                else:
                    pointsOneGreaterFifteen = pointsOneGreaterFifteen + 1
                    playerDict[player][week]['BjkIndex'] = 3
                
probZeroOne = transitionZeroOne/CountOne
probOneOne = 1-probZeroOne
probOneZero = transitionOneZero/CountZero
probZeroZero = 1-probOneZero

row = [0,0,1,1]
col = [0,1,0,1]
transProb = [probZeroZero,probOneZero,probZeroOne,probOneOne]
Aij = csr_matrix((transProb, (row, col)), shape=(2, 2)).toarray()

row = [0,0,0,0,1,1,1,1]
col = [0,1,2,3,0,1,2,3]
emitZero = [pointsZeroLessFive,pointsZeroLessTen,pointsZeroLessFifteen,pointsZeroGreaterFifteen]
emitProbZero = [x/CountZero for x in emitZero]
emitOne = [pointsOneLessFive,pointsOneLessTen,pointsOneLessFifteen,pointsOneGreaterFifteen]
emitProbOne = [x/CountOne for x in emitOne]
emitProb = emitProbZero + emitProbOne
Bjk = csr_matrix((emitProb, (row, col)), shape=(2, 4)).toarray()

def startHMM(playerDict,Aij,Bjk,predictWeek):
    actualDreamTeam = []
    ourPredictPlayers = []
    for player in playerDict:
        weeks = list(sorted(playerDict[player].keys()))
        if (playerDict[player][weeks[0]]['DreamTeam'] == 1):
            oneState = 1
            zeroState = 0
        else:
            oneState = 0
            zeroState = 1
        for week in playerDict[player]:
            if (week < predictWeek):
                if ('BjkIndex' in playerDict[player][week]):
                    emitIndex = playerDict[player][week]['BjkIndex']
                    emitProb = Bjk[1][emitIndex]
                    oneState = zeroState*Aij[0][1]*emitProb + oneState*Aij[1][1]*emitProb
                    emitProb = Bjk[0][emitIndex]
                    zeroState = zeroState*Aij[0][0]*emitProb + oneState*Aij[1][0]*emitProb
            else:
                break
        if (predictWeek-1 in playerDict[player]):
            if (oneState > zeroState):
                score = []
                score.append(oneState/(oneState+zeroState))
                score.append(player)
                ourPredictPlayers.append(score)
            if (playerDict[player][predictWeek-1]['DreamTeam'] > 0):
                actualDreamTeam.append(player)

    ourPredictPlayers = sorted(ourPredictPlayers, key=itemgetter(0), reverse=True)
    inc = 0
    ourGuyInTeam = 0
    finalPredicted = []
    for player in ourPredictPlayers:
        if(inc < 11):
            finalPredicted.append(player[1])
            if(playerDict[player[1]][predictWeek-1]['DreamTeam'] == 1):
                ourGuyInTeam = ourGuyInTeam + 1
            inc = inc + 1
        else:
            break
                
    precision = ourGuyInTeam/inc
    
    line = np.array([predictWeek,precision])
    
    return line, finalPredicted, actualDreamTeam

rateMatrix = np.empty([1,2])
actualWeeklyDreamTeam = []
weekPredictPlayers = []
for predictWeek in range(7,39):
    line, ourPredictPlayers, actualDreamTeam = startHMM(playerDict,Aij,Bjk,predictWeek)
    rateMatrix = np.vstack([rateMatrix,line])
    weekPredictPlayers.append(ourPredictPlayers)
    actualWeeklyDreamTeam.append(actualDreamTeam)
    
with open("PredictedPlayers.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(weekPredictPlayers)

with open("ActualDreamTeam.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(actualWeeklyDreamTeam)
    
rateMatrix = np.delete(rateMatrix, 0, 0)
np.savetxt("PredictedRates.csv", rateMatrix, delimiter=",")