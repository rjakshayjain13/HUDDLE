#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:24:57 2017

@author: ishanshrivastava
"""
from urllib.request import urlopen
import json
import pandas as pd
from collections import defaultdict
import time
#phases
#elements --> These are players probably
#stats --> Has some headings
#game-settings --> Has informatiion regarding formations
#"current-event": 8,
#"total-players": 5224549,
#"teams" --> 20 Teams
#element_types --> GoalKeeper,Midfielder, Defender, Forward ids
#"last-entry-event": 38,
#"stats_options"-->
#next_event_fixtures
#events
#next-event

#url = 'https://fantasy.premierleague.com/drf/bootstrap'
#response = urlopen(url)
#data = response.read()
#jsonData = json.loads(data.decode("utf-8"))
#
#playersDataFrame = pd.DataFrame(jsonData.get('elements'))
#teamsDataFrame = pd.DataFrame(jsonData.get('teams'))
#playersDataFrame.to_csv('players.csv')

""""""""""""""""""""""""""""""""""""""""""""
t1 = time.time()

#dataPath = "/Users/ishanshrivastava/Documents/Masters At ASU/Fall Sem 2017/Statistical Machine Learning/Project/SML_Project/Data/"

#FPL16_GW5 = pd.read_csv(dataPath+"FPL16-GW5.csv").iloc[:,0:44]
#FPL16_GW5.loc[:,'Week'] = 5
#FPL16_GW6 = pd.read_csv(dataPath+"FPL16-GW6.csv").iloc[:,0:44]
#FPL16_GW6.loc[:,'Week'] = 6
#frames = [FPL16_GW5, FPL16_GW6]
#FPL16_GW5 = pd.concat(frames)

FPL16 = pd.DataFrame()
frames = [0]*len(range(5,38))
for i in range(5,38):
    df = pd.read_csv("FPL16-GW"+str(i)+".csv").iloc[:,0:44]
    df.loc[:,'Week'] = i
    frames[i-5]=df
    
FPL16 = pd.concat(frames)

t3 = time.time()
playerDict = defaultdict(defaultdict)
playerPointsLastRoundDict = defaultdict(defaultdict)
playerYellowCardsdDict = defaultdict(defaultdict)
playerGoalsConcededDict = defaultdict(defaultdict)
playerGoalsConcededPointsDict = defaultdict(defaultdict)
playerSavesDict = defaultdict(defaultdict)
playerSavesPointsDict = defaultdict(defaultdict)
playerGoalsScoredDict = defaultdict(defaultdict)
playerGoalsScoredPointsDict = defaultdict(defaultdict)
playerPenaltiesMissedDict = defaultdict(defaultdict)
playerCleanSheetsDict = defaultdict(defaultdict)
playerCleanSheetPointsDict = defaultdict(defaultdict)
playerAssistsdDict = defaultdict(defaultdict)
playerOwnGoalsDict = defaultdict(defaultdict)
playerPenaltiesSavedDict = defaultdict(defaultdict)
playerRedCardsDict = defaultdict(defaultdict)
playerMinutesPlayedDict = defaultdict(defaultdict)
playerSurname=defaultdict(str)
playerFirstName=defaultdict(str)
playerPosition=defaultdict(str)
playerTeam=defaultdict(str)

for row in FPL16.itertuples():
    surname=row.Surname
    firstName=row.FirstName
    playerDict[surname+row.PositionsList+row.Team][row.Week]=row.DreamteamCount
    playerPointsLastRoundDict[surname+row.PositionsList+row.Team][row.Week]=row.PointsLastRound
    playerYellowCardsdDict[surname+row.PositionsList+row.Team][row.Week]=row.YellowCards
    playerGoalsConcededDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsConceded
#    playerGoalsConcededPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsConcededPoints
    playerSavesDict[surname+row.PositionsList+row.Team][row.Week]=row.Saves
#    playerSavesPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.SavesPoints
    playerGoalsScoredDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScored
#    playerGoalsScoredPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScoredPoints
    playerPenaltiesMissedDict[surname+row.PositionsList+row.Team][row.Week]=row.PenaltiesMissed
    playerCleanSheetsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheets
#    playerCleanSheetPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheetPoints
    playerAssistsdDict[surname+row.PositionsList+row.Team][row.Week]=row.Assists
    playerOwnGoalsDict[surname+row.PositionsList+row.Team][row.Week]=row.OwnGoals
    playerPenaltiesSavedDict[surname+row.PositionsList+row.Team][row.Week]=row.PenaltiesSaved
    playerRedCardsDict[surname+row.PositionsList+row.Team][row.Week]=row.RedCards
    playerMinutesPlayedDict[surname+row.PositionsList+row.Team][row.Week]=row.MinutesPlayed
    playerSurname[surname+row.PositionsList+row.Team]=surname
    playerFirstName[surname+row.PositionsList+row.Team]=row.FirstName
    playerPosition[surname+row.PositionsList+row.Team]=row.PositionsList
    playerTeam[surname+row.PositionsList+row.Team]=row.Team

playerDict1 = defaultdict(defaultdict)#DreamteamCount
playerDict2 = defaultdict(defaultdict)#PointsLastRound
playerDict3 = defaultdict(defaultdict)#YellowCards
playerDict4 = defaultdict(defaultdict)#GoalsConceded
playerDict5 = defaultdict(defaultdict)#Saves
playerDict6 = defaultdict(defaultdict)#GoalsScored
playerDict7 = defaultdict(defaultdict)#PenaltiesMissed
playerDict8 = defaultdict(defaultdict)#CleanSheets
playerDict9 = defaultdict(defaultdict)#Assists
playerDict10 = defaultdict(defaultdict)#OwnGoals
playerDict11 = defaultdict(defaultdict)#PenaltiesSaved
playerDict12 = defaultdict(defaultdict)#RedCards
playerDict13 = defaultdict(defaultdict)#MinutesPlayed

for player,dic in playerDict.items():
    dic2 = playerPointsLastRoundDict.get(player)
    dic3 = playerYellowCardsdDict.get(player)   
    dic4 = playerGoalsConcededDict.get(player)   
    dic5 = playerSavesDict.get(player)   
    dic6 = playerGoalsScoredDict.get(player)   
    dic7 = playerPenaltiesMissedDict.get(player)   
    dic8 = playerCleanSheetsDict.get(player)   
    dic9 = playerAssistsdDict.get(player)   
    dic10 = playerOwnGoalsDict.get(player)   
    dic11= playerPenaltiesSavedDict.get(player)   
    dic12 = playerRedCardsDict.get(player)   
    dic13 = playerMinutesPlayedDict.get(player)   
    for i in range(5,38):
        if i == 5:
            if None != dic.get(i+1) and None != dic.get(i):
                playerDict1[player][i]=dic.get(i+1)-dic.get(i)
            if None != dic2.get(i+1) and None != dic2.get(i):
                playerDict2[player][i]=dic2.get(i)
            if None != dic3.get(i):
                playerDict3[player][i]=dic3.get(i)
            if None != dic4.get(i):
                playerDict4[player][i]=dic4.get(i)
            if None != dic5.get(i):
                playerDict5[player][i]=dic5.get(i)
            if None != dic6.get(i):
                playerDict6[player][i]=dic6.get(i)
            if None != dic7.get(i):
                playerDict7[player][i]=dic7.get(i)
            if None != dic8.get(i):
                playerDict8[player][i]=dic8.get(i)
            if None != dic9.get(i):
                playerDict9[player][i]=dic9.get(i)
            if None != dic10.get(i):
                playerDict10[player][i]=dic10.get(i)
            if None != dic11.get(i):
                playerDict11[player][i]=dic11.get(i)
            if None != dic12.get(i):
                playerDict12[player][i]=dic12.get(i)
            if None != dic13.get(i):
                playerDict13[player][i]=dic13.get(i)
            if None != dic3.get(i+1) and None != dic3.get(i):
                playerDict3[player][i+1]=dic3.get(i+1)-dic3.get(i)
            if None != dic4.get(i+1) and None != dic4.get(i):
                playerDict4[player][i+1]=dic4.get(i+1)-dic4.get(i)
            if None != dic5.get(i+1) and None != dic5.get(i):
                playerDict5[player][i+1]=dic5.get(i+1)-dic5.get(i)
            if None != dic6.get(i+1) and None != dic6.get(i):
                playerDict6[player][i+1]=dic6.get(i+1)-dic6.get(i)
            if None != dic7.get(i+1) and None != dic7.get(i):
                playerDict7[player][i+1]=dic7.get(i+1)-dic7.get(i)
            if None != dic8.get(i+1) and None != dic8.get(i):
                playerDict8[player][i+1]=dic8.get(i+1)-dic8.get(i)
            if None != dic9.get(i+1) and None != dic9.get(i):
                playerDict9[player][i+1]=dic9.get(i+1)-dic9.get(i)
            if None != dic10.get(i+1) and None != dic10.get(i):
                playerDict10[player][i+1]=dic10.get(i+1)-dic10.get(i)
            if None != dic11.get(i+1) and None != dic11.get(i):
                playerDict11[player][i+1]=dic11.get(i+1)-dic11.get(i)
            if None != dic12.get(i+1) and None != dic12.get(i):
                playerDict12[player][i+1]=dic12.get(i+1)-dic12.get(i)
            if None != dic13.get(i+1) and None != dic13.get(i):
                playerDict13[player][i+1]=dic13.get(i+1)-dic13.get(i)
        else:
            if None != dic.get(i+1) and None != dic.get(i):
                playerDict1[player][i]=dic.get(i+1)-dic.get(i)
            if None != dic2.get(i+1) and None != dic2.get(i):
                playerDict2[player][i]=dic2.get(i)
            if None != dic3.get(i+1) and None != dic3.get(i):
                playerDict3[player][i+1]=dic3.get(i+1)-dic3.get(i)
            if None != dic4.get(i+1) and None != dic4.get(i):
                playerDict4[player][i+1]=dic4.get(i+1)-dic4.get(i)
            if None != dic5.get(i+1) and None != dic5.get(i):
                playerDict5[player][i+1]=dic5.get(i+1)-dic5.get(i)
            if None != dic6.get(i+1) and None != dic6.get(i):
                playerDict6[player][i+1]=dic6.get(i+1)-dic6.get(i)
            if None != dic7.get(i+1) and None != dic7.get(i):
                playerDict7[player][i+1]=dic7.get(i+1)-dic7.get(i)
            if None != dic8.get(i+1) and None != dic8.get(i):
                playerDict8[player][i+1]=dic8.get(i+1)-dic8.get(i)
            if None != dic9.get(i+1) and None != dic9.get(i):
                playerDict9[player][i+1]=dic9.get(i+1)-dic9.get(i)
            if None != dic10.get(i+1) and None != dic10.get(i):
                playerDict10[player][i+1]=dic10.get(i+1)-dic10.get(i)
            if None != dic11.get(i+1) and None != dic11.get(i):
                playerDict11[player][i+1]=dic11.get(i+1)-dic11.get(i)
            if None != dic12.get(i+1) and None != dic12.get(i):
                playerDict12[player][i+1]=dic12.get(i+1)-dic12.get(i)
            if None != dic13.get(i+1) and None != dic13.get(i):
                playerDict13[player][i+1]=dic13.get(i+1)-dic13.get(i)
        

FPL16_Cleaned = pd.DataFrame(columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
i=1
for player,dic in playerDict1.items():
    for week,dreatTeam in dic.items():
#        print(i)
        pointsLastRound=playerDict2.get(player).get(week)
        yellowCards=playerDict3.get(player).get(week)
        goalsConceded=playerDict4.get(player).get(week)
        saves=playerDict5.get(player).get(week) 
        goalsScored=playerDict6.get(player).get(week) 
        penaltiesMissed=playerDict7.get(player).get(week) 
        cleanSheets=playerDict8.get(player).get(week)
        assists=playerDict9.get(player).get(week) 
        ownGoals=playerDict10.get(player).get(week) 
        penaltiesSaved=playerDict11.get(player).get(week)
        redCards=playerDict12.get(player).get(week) 
        minutesPlayed=playerDict13.get(player).get(week)
        df1 = pd.DataFrame([[player,playerFirstName.get(player),playerSurname.get(player),playerPosition.get(player),playerTeam.get(player),week,dreatTeam,pointsLastRound,
                             yellowCards,goalsConceded,saves,goalsScored,
                             penaltiesMissed,cleanSheets,assists,ownGoals,
                             penaltiesSaved,redCards,minutesPlayed]], columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
        FPL16_Cleaned=FPL16_Cleaned.append(df1)
#        i=i+1

FPL16_Cleaned_Cummilative = pd.DataFrame(columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
i=1
for player,dic in playerDict1.items():
    for week,dreatTeam in dic.items():
#        print(i)
        pointsLastRound=playerPointsLastRoundDict.get(player).get(week)
        yellowCards=playerYellowCardsdDict.get(player).get(week)
        goalsConceded=playerGoalsConcededDict.get(player).get(week)
        saves=playerSavesDict.get(player).get(week) 
        goalsScored=playerGoalsScoredDict.get(player).get(week) 
        penaltiesMissed=playerPenaltiesMissedDict.get(player).get(week) 
        cleanSheets=playerCleanSheetsDict.get(player).get(week)
        assists=playerAssistsdDict.get(player).get(week) 
        ownGoals=playerOwnGoalsDict.get(player).get(week) 
        penaltiesSaved=playerPenaltiesSavedDict.get(player).get(week)
        redCards=playerRedCardsDict.get(player).get(week) 
        minutesPlayed=playerMinutesPlayedDict.get(player).get(week)
        df1 = pd.DataFrame([[player,playerFirstName.get(player),playerSurname.get(player),playerPosition.get(player),playerTeam.get(player),week,dreatTeam,pointsLastRound,
                             yellowCards,goalsConceded,saves,goalsScored,
                             penaltiesMissed,cleanSheets,assists,ownGoals,
                             penaltiesSaved,redCards,minutesPlayed]], columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
        FPL16_Cleaned_Cummilative=FPL16_Cleaned_Cummilative.append(df1)
#        i=i+1


FPL16_Cleaned.to_csv('FPL16_Cleaned.csv')
FPL16_Cleaned_Cummilative.to_csv('FPL16_Cleaned_Cummilative.csv')
t4 = time.time()

print('Time Taken to Clean FPL16 Data: '+str(t4-t3))
"""""""""""""""""""""""""""""""""""
Code for FPL17_Cleaned dataframe
"""""""""""""""""""""""""""""""""""

FPL17 = pd.DataFrame()
frames = [0]*len(range(0,11))
for i in range(0,11):
    df = pd.read_csv("FPL17-GW"+str(i)+".csv").iloc[:,0:44]
    df.loc[:,'Week'] = i
    frames[i]=df
    
FPL17 = pd.concat(frames)
FPL17 = FPL17.append(FPL16[FPL16['Week']==37])


t5 = time.time()

playerFPL17Dict = defaultdict(defaultdict)
playerFPL17PointsLastRoundDict = defaultdict(defaultdict)
playerFPL17YellowCardsdDict = defaultdict(defaultdict)
playerFPL17GoalsConcededDict = defaultdict(defaultdict)
playerFPL17GoalsConcededPointsDict = defaultdict(defaultdict)
playerFPL17SavesDict = defaultdict(defaultdict)
playerFPL17SavesPointsDict = defaultdict(defaultdict)
playerFPL17GoalsScoredDict = defaultdict(defaultdict)
playerFPL17GoalsScoredPointsDict = defaultdict(defaultdict)
playerFPL17PenaltiesMissedDict = defaultdict(defaultdict)
playerFPL17CleanSheetsDict = defaultdict(defaultdict)
playerFPL17CleanSheetPointsDict = defaultdict(defaultdict)
playerFPL17AssistsdDict = defaultdict(defaultdict)
playerFPL17OwnGoalsDict = defaultdict(defaultdict)
playerFPL17PenaltiesSavedDict = defaultdict(defaultdict)
playerFPL17RedCardsDict = defaultdict(defaultdict)
playerFPL17MinutesPlayedDict = defaultdict(defaultdict)
playerFPL17Surname=defaultdict(str)
playerFPL17FirstName=defaultdict(str)
playerFPL17Position=defaultdict(str)
playerFPL17Team=defaultdict(str)

for row in FPL17.itertuples():
    surname=row.Surname
    firstName=row.FirstName
    playerFPL17Dict[surname+row.PositionsList+row.Team][row.Week]=row.DreamteamCount
    playerFPL17PointsLastRoundDict[surname+row.PositionsList+row.Team][row.Week]=row.PointsLastRound
    playerFPL17YellowCardsdDict[surname+row.PositionsList+row.Team][row.Week]=row.YellowCards
    playerFPL17GoalsConcededDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsConceded
#    playerFPL17GoalsConcededPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsConcededPoints
    playerFPL17SavesDict[surname+row.PositionsList+row.Team][row.Week]=row.Saves
#    playerFPL17SavesPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.SavesPoints
    playerFPL17GoalsScoredDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScored
#    playerFPL17GoalsScoredPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScoredPoints
    playerFPL17PenaltiesMissedDict[surname+row.PositionsList+row.Team][row.Week]=row.PenaltiesMissed
    playerFPL17CleanSheetsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheets
#    playerFPL17CleanSheetPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheetPoints
    playerFPL17AssistsdDict[surname+row.PositionsList+row.Team][row.Week]=row.Assists
    playerFPL17OwnGoalsDict[surname+row.PositionsList+row.Team][row.Week]=row.OwnGoals
    playerFPL17PenaltiesSavedDict[surname+row.PositionsList+row.Team][row.Week]=row.PenaltiesSaved
    playerFPL17RedCardsDict[surname+row.PositionsList+row.Team][row.Week]=row.RedCards
    playerFPL17MinutesPlayedDict[surname+row.PositionsList+row.Team][row.Week]=row.MinutesPlayed
    playerFPL17Surname[surname+row.PositionsList+row.Team]=surname
    playerFPL17FirstName[surname+row.PositionsList+row.Team]=row.FirstName
    playerFPL17Position[surname+row.PositionsList+row.Team]=row.PositionsList
    playerFPL17Team[surname+row.PositionsList+row.Team]=row.Team

playerFPL17Dict1 = defaultdict(defaultdict)#DreamteamCount
playerFPL17Dict2 = defaultdict(defaultdict)#PointsLastRound
playerFPL17Dict3 = defaultdict(defaultdict)#YellowCards
playerFPL17Dict4 = defaultdict(defaultdict)#GoalsConceded
playerFPL17Dict5 = defaultdict(defaultdict)#Saves
playerFPL17Dict6 = defaultdict(defaultdict)#GoalsScored
playerFPL17Dict7 = defaultdict(defaultdict)#PenaltiesMissed
playerFPL17Dict8 = defaultdict(defaultdict)#CleanSheets
playerFPL17Dict9 = defaultdict(defaultdict)#Assists
playerFPL17Dict10 = defaultdict(defaultdict)#OwnGoals
playerFPL17Dict11 = defaultdict(defaultdict)#PenaltiesSaved
playerFPL17Dict12 = defaultdict(defaultdict)#RedCards
playerFPL17Dict13 = defaultdict(defaultdict)#MinutesPlayed

for playerFPL17,dic in playerFPL17Dict.items():
    dic2 = playerFPL17PointsLastRoundDict.get(playerFPL17)
    dic3 = playerFPL17YellowCardsdDict.get(playerFPL17)   
    dic4 = playerFPL17GoalsConcededDict.get(playerFPL17)   
    dic5 = playerFPL17SavesDict.get(playerFPL17)   
    dic6 = playerFPL17GoalsScoredDict.get(playerFPL17)   
    dic7 = playerFPL17PenaltiesMissedDict.get(playerFPL17)   
    dic8 = playerFPL17CleanSheetsDict.get(playerFPL17)   
    dic9 = playerFPL17AssistsdDict.get(playerFPL17)   
    dic10 = playerFPL17OwnGoalsDict.get(playerFPL17)   
    dic11= playerFPL17PenaltiesSavedDict.get(playerFPL17)   
    dic12 = playerFPL17RedCardsDict.get(playerFPL17)   
    dic13 = playerFPL17MinutesPlayedDict.get(playerFPL17)   
    for i in range(-1,11):
        if i == -1:
            if None != dic.get(i+1) and None != dic.get(i):
                playerFPL17Dict1[playerFPL17][i]=dic.get(i+1)-dic.get(i)
            if None != dic2.get(i+1) and None != dic2.get(i):
                playerFPL17Dict2[playerFPL17][i]=dic2.get(i)
            if None != dic3.get(i):
                playerFPL17Dict3[playerFPL17][i]=dic3.get(i)
            if None != dic4.get(i):
                playerFPL17Dict4[playerFPL17][i]=dic4.get(i)
            if None != dic5.get(i):
                playerFPL17Dict5[playerFPL17][i]=dic5.get(i)
            if None != dic6.get(i):
                playerFPL17Dict6[playerFPL17][i]=dic6.get(i)
            if None != dic7.get(i):
                playerFPL17Dict7[playerFPL17][i]=dic7.get(i)
            if None != dic8.get(i):
                playerFPL17Dict8[playerFPL17][i]=dic8.get(i)
            if None != dic9.get(i):
                playerFPL17Dict9[playerFPL17][i]=dic9.get(i)
            if None != dic10.get(i):
                playerFPL17Dict10[playerFPL17][i]=dic10.get(i)
            if None != dic11.get(i):
                playerFPL17Dict11[playerFPL17][i]=dic11.get(i)
            if None != dic12.get(i):
                playerFPL17Dict12[playerFPL17][i]=dic12.get(i)
            if None != dic13.get(i):
                playerFPL17Dict13[playerFPL17][i]=dic13.get(i)
            if None != dic3.get(i+1) and None != dic3.get(i):
                playerFPL17Dict3[playerFPL17][i+1]=dic3.get(i+1)-dic3.get(i)
            if None != dic4.get(i+1) and None != dic4.get(i):
                playerFPL17Dict4[playerFPL17][i+1]=dic4.get(i+1)-dic4.get(i)
            if None != dic5.get(i+1) and None != dic5.get(i):
                playerFPL17Dict5[playerFPL17][i+1]=dic5.get(i+1)-dic5.get(i)
            if None != dic6.get(i+1) and None != dic6.get(i):
                playerFPL17Dict6[playerFPL17][i+1]=dic6.get(i+1)-dic6.get(i)
            if None != dic7.get(i+1) and None != dic7.get(i):
                playerFPL17Dict7[playerFPL17][i+1]=dic7.get(i+1)-dic7.get(i)
            if None != dic8.get(i+1) and None != dic8.get(i):
                playerFPL17Dict8[playerFPL17][i+1]=dic8.get(i+1)-dic8.get(i)
            if None != dic9.get(i+1) and None != dic9.get(i):
                playerFPL17Dict9[playerFPL17][i+1]=dic9.get(i+1)-dic9.get(i)
            if None != dic10.get(i+1) and None != dic10.get(i):
                playerFPL17Dict10[playerFPL17][i+1]=dic10.get(i+1)-dic10.get(i)
            if None != dic11.get(i+1) and None != dic11.get(i):
                playerFPL17Dict11[playerFPL17][i+1]=dic11.get(i+1)-dic11.get(i)
            if None != dic12.get(i+1) and None != dic12.get(i):
                playerFPL17Dict12[playerFPL17][i+1]=dic12.get(i+1)-dic12.get(i)
            if None != dic13.get(i+1) and None != dic13.get(i):
                playerFPL17Dict13[playerFPL17][i+1]=dic13.get(i+1)-dic13.get(i)
        else:
            if None != dic.get(i+1) and None != dic.get(i):
                playerFPL17Dict1[playerFPL17][i]=dic.get(i+1)-dic.get(i)
            if None != dic2.get(i+1) and None != dic2.get(i):
                playerFPL17Dict2[playerFPL17][i]=dic2.get(i)
            if None != dic3.get(i+1) and None != dic3.get(i):
                playerFPL17Dict3[playerFPL17][i+1]=dic3.get(i+1)-dic3.get(i)
            if None != dic4.get(i+1) and None != dic4.get(i):
                playerFPL17Dict4[playerFPL17][i+1]=dic4.get(i+1)-dic4.get(i)
            if None != dic5.get(i+1) and None != dic5.get(i):
                playerFPL17Dict5[playerFPL17][i+1]=dic5.get(i+1)-dic5.get(i)
            if None != dic6.get(i+1) and None != dic6.get(i):
                playerFPL17Dict6[playerFPL17][i+1]=dic6.get(i+1)-dic6.get(i)
            if None != dic7.get(i+1) and None != dic7.get(i):
                playerFPL17Dict7[playerFPL17][i+1]=dic7.get(i+1)-dic7.get(i)
            if None != dic8.get(i+1) and None != dic8.get(i):
                playerFPL17Dict8[playerFPL17][i+1]=dic8.get(i+1)-dic8.get(i)
            if None != dic9.get(i+1) and None != dic9.get(i):
                playerFPL17Dict9[playerFPL17][i+1]=dic9.get(i+1)-dic9.get(i)
            if None != dic10.get(i+1) and None != dic10.get(i):
                playerFPL17Dict10[playerFPL17][i+1]=dic10.get(i+1)-dic10.get(i)
            if None != dic11.get(i+1) and None != dic11.get(i):
                playerFPL17Dict11[playerFPL17][i+1]=dic11.get(i+1)-dic11.get(i)
            if None != dic12.get(i+1) and None != dic12.get(i):
                playerFPL17Dict12[playerFPL17][i+1]=dic12.get(i+1)-dic12.get(i)
            if None != dic13.get(i+1) and None != dic13.get(i):
                playerFPL17Dict13[playerFPL17][i+1]=dic13.get(i+1)-dic13.get(i)
        

FPL17_Cleaned = pd.DataFrame(columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
i=1
for playerFPL17,dic in playerFPL17Dict1.items():
    for week,dreatTeam in dic.items():
#        print(i)
        pointsLastRound=playerFPL17Dict2.get(playerFPL17).get(week)
        yellowCards=playerFPL17Dict3.get(playerFPL17).get(week)
        goalsConceded=playerFPL17Dict4.get(playerFPL17).get(week)
        saves=playerFPL17Dict5.get(playerFPL17).get(week) 
        goalsScored=playerFPL17Dict6.get(playerFPL17).get(week) 
        penaltiesMissed=playerFPL17Dict7.get(playerFPL17).get(week) 
        cleanSheets=playerFPL17Dict8.get(playerFPL17).get(week)
        assists=playerFPL17Dict9.get(playerFPL17).get(week) 
        ownGoals=playerFPL17Dict10.get(playerFPL17).get(week) 
        penaltiesSaved=playerFPL17Dict11.get(playerFPL17).get(week)
        redCards=playerFPL17Dict12.get(playerFPL17).get(week) 
        minutesPlayed=playerFPL17Dict13.get(playerFPL17).get(week)
        df1 = pd.DataFrame([[playerFPL17,playerFPL17FirstName.get(playerFPL17),playerFPL17Surname.get(playerFPL17),playerFPL17Position.get(playerFPL17),playerFPL17Team.get(playerFPL17),week,dreatTeam,pointsLastRound,
                             yellowCards,goalsConceded,saves,goalsScored,
                             penaltiesMissed,cleanSheets,assists,ownGoals,
                             penaltiesSaved,redCards,minutesPlayed]], columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
        FPL17_Cleaned=FPL17_Cleaned.append(df1)
#        i=i+1

FPL17_Cleaned_Cummilative = pd.DataFrame(columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
i=1
for playerFPL17,dic in playerFPL17Dict1.items():
    for week,dreatTeam in dic.items():
#        print(i)
        pointsLastRound=playerFPL17PointsLastRoundDict.get(playerFPL17).get(week)
        yellowCards=playerFPL17YellowCardsdDict.get(playerFPL17).get(week)
        goalsConceded=playerFPL17GoalsConcededDict.get(playerFPL17).get(week)
        saves=playerFPL17SavesDict.get(playerFPL17).get(week) 
        goalsScored=playerFPL17GoalsScoredDict.get(playerFPL17).get(week) 
        penaltiesMissed=playerFPL17PenaltiesMissedDict.get(playerFPL17).get(week) 
        cleanSheets=playerFPL17CleanSheetsDict.get(playerFPL17).get(week)
        assists=playerFPL17AssistsdDict.get(playerFPL17).get(week) 
        ownGoals=playerFPL17OwnGoalsDict.get(playerFPL17).get(week) 
        penaltiesSaved=playerFPL17PenaltiesSavedDict.get(playerFPL17).get(week)
        redCards=playerFPL17RedCardsDict.get(playerFPL17).get(week) 
        minutesPlayed=playerFPL17MinutesPlayedDict.get(playerFPL17).get(week)
        df1 = pd.DataFrame([[playerFPL17,playerFPL17FirstName.get(playerFPL17),playerFPL17Surname.get(playerFPL17),playerFPL17Position.get(playerFPL17),playerFPL17Team.get(playerFPL17),week,dreatTeam,pointsLastRound,
                             yellowCards,goalsConceded,saves,goalsScored,
                             penaltiesMissed,cleanSheets,assists,ownGoals,
                             penaltiesSaved,redCards,minutesPlayed]], columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
        FPL17_Cleaned_Cummilative=FPL17_Cleaned_Cummilative.append(df1)
#        i=i+1

FPL17_Cleaned1=FPL17_Cleaned[FPL17_Cleaned['Week']!=-1]
FPL17_Cleaned_Cummilative1=FPL17_Cleaned_Cummilative[FPL17_Cleaned_Cummilative['Week']!=-1]
FPL17_Cleaned1.to_csv('FPL17_Cleaned.csv')
FPL17_Cleaned_Cummilative1.to_csv('FPL17_Cleaned_Cummilative.csv')

#playerFPL17Dict = defaultdict(defaultdict)
#playerFPL17PointsLastRoundDict = defaultdict(defaultdict)
#playerFPL17YellowCardsdDict = defaultdict(defaultdict)
#playerFPL17GoalsConcededDict = defaultdict(defaultdict)
#playerFPL17GoalsConcededPointsDict = defaultdict(defaultdict)
#playerFPL17SavesDict = defaultdict(defaultdict)
#playerFPL17SavesPointsDict = defaultdict(defaultdict)
#playerFPL17GoalsScoredDict = defaultdict(defaultdict)
#playerFPL17GoalsScoredPointsDict = defaultdict(defaultdict)
#playerFPL17PenaltiesMissedDict = defaultdict(defaultdict)
#playerFPL17CleanSheetsDict = defaultdict(defaultdict)
#playerFPL17CleanSheetPointsDict = defaultdict(defaultdict)
#playerFPL17AssistsdDict = defaultdict(defaultdict)
#playerFPL17OwnGoalsDict = defaultdict(defaultdict)
#playerFPL17PenaltiesSavedDict = defaultdict(defaultdict)
#playerFPL17RedCardsDict = defaultdict(defaultdict)
#playerFPL17MinutesPlayedDict = defaultdict(defaultdict)
#
#for row in FPL17.itertuples():
#    surname=row.Surname
#    firstName=row.FirstName
#    playerFPL17Dict[surname+row.PositionsList+row.Team][row.Week]=row.DreamteamCount
#    playerFPL17PointsLastRoundDict[surname+row.PositionsList+row.Team][row.Week]=row.PointsLastRound
#    playerFPL17YellowCardsdDict[surname+row.PositionsList+row.Team][row.Week]=row.YellowCards
#    playerFPL17GoalsConcededDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsConceded
##    playerFPL17GoalsConcededPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsConcededPoints
#    playerFPL17SavesDict[surname+row.PositionsList+row.Team][row.Week]=row.Saves
##    playerFPL17SavesPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.SavesPoints
#    playerFPL17GoalsScoredDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScored
##    playerFPL17GoalsScoredPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScoredPoints
#    playerFPL17PenaltiesMissedDict[surname+row.PositionsList+row.Team][row.Week]=row.PenaltiesMissed
#    playerFPL17CleanSheetsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheets
##    playerFPL17CleanSheetPointsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheetPoints
#    playerFPL17AssistsdDict[surname+row.PositionsList+row.Team][row.Week]=row.Assists
#    playerFPL17OwnGoalsDict[surname+row.PositionsList+row.Team][row.Week]=row.OwnGoals
#    playerFPL17PenaltiesSavedDict[surname+row.PositionsList+row.Team][row.Week]=row.PenaltiesSaved
#    playerFPL17RedCardsDict[surname+row.PositionsList+row.Team][row.Week]=row.RedCards
#    playerFPL17MinutesPlayedDict[surname+row.PositionsList+row.Team][row.Week]=row.MinutesPlayed
#    
#playerFPL17Dict1 = defaultdict(defaultdict)#DreamteamCount
#playerFPL17Dict2 = defaultdict(defaultdict)#PointsLastRound
#playerFPL17Dict3 = defaultdict(defaultdict)#YellowCards
#playerFPL17Dict4 = defaultdict(defaultdict)#GoalsConceded
#playerFPL17Dict5 = defaultdict(defaultdict)#Saves
#playerFPL17Dict6 = defaultdict(defaultdict)#GoalsScored
#playerFPL17Dict7 = defaultdict(defaultdict)#PenaltiesMissed
#playerFPL17Dict8 = defaultdict(defaultdict)#CleanSheets
#playerFPL17Dict9 = defaultdict(defaultdict)#Assists
#playerFPL17Dict10 = defaultdict(defaultdict)#OwnGoals
#playerFPL17Dict11 = defaultdict(defaultdict)#PenaltiesSaved
#playerFPL17Dict12 = defaultdict(defaultdict)#RedCards
#playerFPL17Dict13 = defaultdict(defaultdict)#MinutesPlayed
#
#for playerFPL17,dic in playerFPL17Dict.items():
#    dic2 = playerFPL17PointsLastRoundDict.get(playerFPL17)
#    dic3 = playerFPL17YellowCardsdDict.get(playerFPL17)   
#    dic4 = playerFPL17GoalsConcededDict.get(playerFPL17)   
#    dic5 = playerFPL17SavesDict.get(playerFPL17)   
#    dic6 = playerFPL17GoalsScoredDict.get(playerFPL17)   
#    dic7 = playerFPL17PenaltiesMissedDict.get(playerFPL17)   
#    dic8 = playerFPL17CleanSheetsDict.get(playerFPL17)   
#    dic9 = playerFPL17AssistsdDict.get(playerFPL17)   
#    dic10 = playerFPL17OwnGoalsDict.get(playerFPL17)   
#    dic11= playerFPL17PenaltiesSavedDict.get(playerFPL17)   
#    dic12 = playerFPL17RedCardsDict.get(playerFPL17)   
#    dic13 = playerFPL17MinutesPlayedDict.get(playerFPL17)   
#    for i in range(-1,11):
#        if None != dic.get(i+1) and None != dic.get(i):
#            playerFPL17Dict1[playerFPL17][i]=dic.get(i+1)-dic.get(i)
#        if None != dic2.get(i+1) and None != dic2.get(i):
#            playerFPL17Dict2[playerFPL17][i+1]=dic2.get(i+1)-dic2.get(i)
#        if None != dic3.get(i+1) and None != dic3.get(i):
#            playerFPL17Dict3[playerFPL17][i+1]=dic3.get(i+1)-dic3.get(i)
#        if None != dic4.get(i+1) and None != dic4.get(i):
#            playerFPL17Dict4[playerFPL17][i+1]=dic4.get(i+1)-dic4.get(i)
#        if None != dic5.get(i+1) and None != dic5.get(i):
#            playerFPL17Dict5[playerFPL17][i+1]=dic5.get(i+1)-dic5.get(i)
#        if None != dic6.get(i+1) and None != dic6.get(i):
#            playerFPL17Dict6[playerFPL17][i+1]=dic6.get(i+1)-dic6.get(i)
#        if None != dic7.get(i+1) and None != dic7.get(i):
#            playerFPL17Dict7[playerFPL17][i+1]=dic7.get(i+1)-dic7.get(i)
#        if None != dic8.get(i+1) and None != dic8.get(i):
#            playerFPL17Dict8[playerFPL17][i+1]=dic8.get(i+1)-dic8.get(i)
#        if None != dic9.get(i+1) and None != dic9.get(i):
#            playerFPL17Dict9[playerFPL17][i+1]=dic9.get(i+1)-dic9.get(i)
#        if None != dic10.get(i+1) and None != dic10.get(i):
#            playerFPL17Dict10[playerFPL17][i+1]=dic10.get(i+1)-dic10.get(i)
#        if None != dic11.get(i+1) and None != dic11.get(i):
#            playerFPL17Dict11[playerFPL17][i+1]=dic11.get(i+1)-dic11.get(i)
#        if None != dic12.get(i+1) and None != dic12.get(i):
#            playerFPL17Dict12[playerFPL17][i+1]=dic12.get(i+1)-dic12.get(i)
#        if None != dic13.get(i+1) and None != dic13.get(i):
#            playerFPL17Dict13[playerFPL17][i+1]=dic13.get(i+1)-dic13.get(i)
#        
#
#FPL17_Cleaned = pd.DataFrame(columns = ['Player','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
#                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
#
#for playerFPL17,dic in playerFPL17Dict1.items():
#    for week,dreatTeam in dic.items():
#        pointsLastRound=playerFPL17Dict2.get(playerFPL17).get(week)
#        yellowCards=playerFPL17Dict3.get(playerFPL17).get(week)
#        goalsConceded=playerFPL17Dict4.get(playerFPL17).get(week)
#        saves=playerFPL17Dict5.get(playerFPL17).get(week) 
#        goalsScored=playerFPL17Dict6.get(playerFPL17).get(week) 
#        penaltiesMissed=playerFPL17Dict7.get(playerFPL17).get(week) 
#        cleanSheets=playerFPL17Dict8.get(playerFPL17).get(week)
#        assists=playerFPL17Dict9.get(playerFPL17).get(week) 
#        ownGoals=playerFPL17Dict10.get(playerFPL17).get(week) 
#        penaltiesSaved=playerFPL17Dict11.get(playerFPL17).get(week)
#        redCards=playerFPL17Dict12.get(playerFPL17).get(week) 
#        minutesPlayed=playerFPL17Dict13.get(playerFPL17).get(week) 
#        df1 = pd.DataFrame([[playerFPL17,week,dreatTeam,pointsLastRound,
#                             yellowCards,goalsConceded,saves,goalsScored,
#                             penaltiesMissed,cleanSheets,assists,ownGoals,
#                             penaltiesSaved,redCards,minutesPlayed]], columns = ['Player','Week','InDreamTeamNextWeek','PointsLastRound','YellowCards','GoalsConceded','Saves',
#                                        'GoalsScored','PenaltiesMissed','CleanSheets','Assists','OwnGoals','PenaltiesSaved','RedCards','MinutesPlayed'])
#        FPL17_Cleaned=FPL17_Cleaned.append(df1)
#
#
#FPL17_Cleaned.to_csv('FPL17_Cleaned.csv')
#t6=time.time()
#print('Time Taken to Clean FPL17 Data: '+str(t6-t5))
#
#t2=time.time()
#print('Total Time Taken: '+str(t2-t1))
#
#Fry_FPL16_Cleaned=FPL16_Cleaned[FPL17_Cleaned['Player']=='FryDEFMID']
#
#FPL17.to_csv('FPL17.csv')