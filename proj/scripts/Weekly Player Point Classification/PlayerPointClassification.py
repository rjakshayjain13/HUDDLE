#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:25:17 2017

@author: ishanshrivastava
"""

import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import time

t1 = time.time()
dataPath = "/Users/ishanshrivastava/Documents/Masters At ASU/Fall Sem 2017/Statistical Machine Learning/Project/"


FPL16=pd.read_csv(dataPath+'FPL16.csv')

global playerPointsLastRoundDict
global playerGoalsScoredDict
global playerCleanSheetsDict
global playerAssistsdDict
global playerSurname
global playerFirstName
global playerPosition
global playerTeam

playerPointsLastRoundDict = defaultdict(defaultdict)
playerGoalsScoredDict = defaultdict(defaultdict)
playerCleanSheetsDict = defaultdict(defaultdict)
playerAssistsdDict = defaultdict(defaultdict)
playerSurname=defaultdict(str)
playerFirstName=defaultdict(str)
playerPosition=defaultdict(str)
playerTeam=defaultdict(str)

def initialize(pointForLabel):
    for row in FPL16.itertuples():
        surname=row.Surname
        firstName=row.FirstName
        playerPointsLastRoundDict[surname+row.PositionsList+row.Team][row.Week]=row.PointsLastRound
        playerGoalsScoredDict[surname+row.PositionsList+row.Team][row.Week]=row.GoalsScored
        playerCleanSheetsDict[surname+row.PositionsList+row.Team][row.Week]=row.CleanSheets
        playerAssistsdDict[surname+row.PositionsList+row.Team][row.Week]=row.Assists
        playerSurname[surname+row.PositionsList+row.Team]=surname
        playerFirstName[surname+row.PositionsList+row.Team]=firstName
        playerPosition[surname+row.PositionsList+row.Team]=row.PositionsList
        playerTeam[surname+row.PositionsList+row.Team]=row.Team
    
    playerDict1 = defaultdict(defaultdict)#Label 1 if PointsLastRound>=7 else 0
    playerDict2 = defaultdict(defaultdict)#PointsLastRound
    playerDict6 = defaultdict(defaultdict)#GoalsScored
    playerDict8 = defaultdict(defaultdict)#CleanSheets
    playerDict9 = defaultdict(defaultdict)#Assists
    
    for player,dic in playerPointsLastRoundDict.items():
        dic6 = playerGoalsScoredDict.get(player) 
        dic8 = playerCleanSheetsDict.get(player)   
        dic9 = playerAssistsdDict.get(player)
        keys = list(dic.keys())
        values = list(dic.values())
        n = len(keys)
        for k in keys:
            ind = keys.index(k)
            if k == keys[0]:
                if ind < n-1 and None != values[ind+1] and None !=values[ind]:
                    nextKey = keys[ind+1]
                    playerDict6[player][nextKey]=dic6.get(nextKey)-dic6.get(k)
                    playerDict8[player][nextKey]=dic8.get(nextKey)-dic8.get(k)
                    playerDict9[player][nextKey]=dic9.get(nextKey)-dic9.get(k)
            else:
                if ind < n-1 and None != values[ind+1] and None !=values[ind]:
                    playerDict2[player][k]=dic.get(k)
                    if values[ind+1]  >= pointForLabel:
                        playerDict1[player][k]=1
                    else:
                        playerDict1[player][k]=0
                    nextKey = keys[ind+1]
                    playerDict6[player][nextKey]=dic6.get(nextKey)-dic6.get(k)
                    playerDict8[player][nextKey]=dic8.get(nextKey)-dic8.get(k)
                    playerDict9[player][nextKey]=dic9.get(nextKey)-dic9.get(k)
                
            
    
    FPL16_Cleaned1 = pd.DataFrame(columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','Label','PointsLastRound'
                                            ,'GoalsScored','CleanSheets','Assists'])
    
    for player,dic in playerDict1.items():
        for week,label in dic.items():
            pointsLastRound=playerDict2.get(player).get(week)
            goalsScored=playerDict6.get(player).get(week)
            cleanSheets=playerDict8.get(player).get(week)
            assists=playerDict9.get(player).get(week) 
            df1 = pd.DataFrame([[player,playerFirstName.get(player),playerSurname.get(player),playerPosition.get(player),playerTeam.get(player),week,label,pointsLastRound,goalsScored,
                                 cleanSheets,assists]], columns = ['PlayerKey','FirstName','Surname','Position','Team','Week','Label','PointsLastRound'
                                            ,'GoalsScored','CleanSheets','Assists'])
            FPL16_Cleaned1=FPL16_Cleaned1.append(df1)
    return FPL16_Cleaned1



"""
Get the Cleaned Data
"""
pointForLabel = 7
FPL16_Cleaned1 = initialize(pointForLabel)
t2 = time.time()
print('Time to Clean the Data '+str(t2-t1))
"""
Naive Bayes
"""
t3 = time.time()
allPlayers = set(FPL16_Cleaned1['PlayerKey'])
weeks = set(FPL16_Cleaned1['Week'])
features = ['PointsLastRound','GoalsScored','CleanSheets','Assists']
resultsOverSeveralWeeks_NB = pd.DataFrame(columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration'])
weeks.remove(list(weeks)[0])

for predictForWeek in weeks:
    results = pd.DataFrame(columns = ['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
    
    #predictForWeek = 37
    playerPredictedToScore = [tuple]
    for player in allPlayers:
        
        playerData = FPL16_Cleaned1[FPL16_Cleaned1['PlayerKey']==player]
        
        if predictForWeek in list(playerData['Week']):
            pointsIn_PredictForWeek = playerData[playerData['Week']==predictForWeek]['PointsLastRound']
        else:
            pointsIn_PredictForWeek = ['Did Not play']
            
        if predictForWeek-1 in list(playerData['Week']):
            playerData_predictOnWeek=playerData[playerData['Week']==predictForWeek-1]
        else:
            continue
        
        playerData = playerData[playerData['Week']<predictForWeek-1]
        if(len(playerData)!=0):
            clf = GaussianNB()
            df = playerData[features]
            features_train = np.array(df.values,dtype=np.float)
            label_train = np.array(playerData['Label'],dtype=np.int)
            clf.fit(features_train, label_train)
            test = np.array(playerData_predictOnWeek[features].values,dtype=np.float)
            res = clf.predict(test)
            if res[0]==1:
                playerPredictedToScore.append(tuple((player,playerFirstName.get(player),playerSurname.get(player))))
            prob = clf.predict_proba(test)
            df1 = pd.DataFrame([[player,prob[0][0],res[0],playerData_predictOnWeek['Label'][0],pointsIn_PredictForWeek[0]]],columns=['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
            results=results.append(df1)
        
    #results.to_csv('results5.csv')
    total = len(results)
    results_actual1 = results[results['actualLabel'] == 1]
    results_actual0 = results[results['actualLabel'] == 0]  
#    acc = sum(results_actual1['predictedLabel'])/len(results_actual1)
    actual0 = len(results_actual0)
    actual1 = len(results_actual1)
    FP = sum(results_actual0['predictedLabel'])
    TN = actual0 - FP
    TP = sum(results_actual1['predictedLabel'])
    FN = actual1 - TP
    
    accuracy = 'Not enough data' if total == 0 else (TP+TN)/total
    specificity = 'Never scored below 5 till this week' if actual0 == 0 else TN/actual0 #When it's actually 0, how often does it predict 0?
    recall_senstivity = 'Never scored above 5 till this week' if actual1 == 0 else TP/actual1 #When it's actually 1, how often does it predict 1?
    precision = 'No 1s predicted' if sum(results['predictedLabel']) ==0 else TP/sum(results['predictedLabel']) #When it predicts yes, how often is it correct?
    playersInConsideration = sum(results['predictedLabel'] == 1)
    playersPrunedOut = sum(results['predictedLabel'] == 0)
    resultsOverSeveralWeeks_NB=resultsOverSeveralWeeks_NB.append(
            pd.DataFrame([[predictForWeek,accuracy,specificity,recall_senstivity,precision,
                           playersInConsideration,playersPrunedOut,playerPredictedToScore]],
        columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration']))
    


resultsOverSeveralWeeks_NB.to_csv('resultsOverSeveralWeeks_NB_'+str(pointForLabel)+'.csv')
t4 = time.time()
print('Time to Run NB '+str(t4-t3))
"""
Logistic Regression
"""
t5 = time.time()
allPlayers = set(FPL16_Cleaned1['PlayerKey'])
weeks = set(FPL16_Cleaned1['Week'])
features = ['PointsLastRound','GoalsScored','CleanSheets','Assists']
resultsOverSeveralWeeks_LR = pd.DataFrame(columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration'])
weeks.remove(list(weeks)[0])

for predictForWeek in weeks:
    results_LR = pd.DataFrame(columns = ['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
    playerPredictedToScore = [tuple]
    for player in allPlayers:
        playerData = FPL16_Cleaned1[FPL16_Cleaned1['PlayerKey']==player]
        
        if predictForWeek in list(playerData['Week']):
            pointsIn_PredictForWeek = playerData[playerData['Week']==predictForWeek]['PointsLastRound']
        else:
            pointsIn_PredictForWeek = ['Did Not play']
            
        if predictForWeek-1 in list(playerData['Week']):
            playerData_predictOnWeek=playerData[playerData['Week']==predictForWeek-1]
        else:
            continue
        
        playerData = playerData[playerData['Week']<predictForWeek-1]
        if(len(playerData)!=0):
            model = LogisticRegression()
            df = playerData[features]
            features_train = np.array(df.values,dtype=np.float)
            label_train = np.array(playerData['Label'],dtype=np.int)
            test = np.array(playerData_predictOnWeek[features].values,dtype=np.float)
            if len(set(label_train)) >1:
                model = model.fit(features_train, label_train)
                pred = model.predict(test)
                prob = model.predict_proba(test)
                if pred[0]==1:
                    playerPredictedToScore.append(tuple((player,playerFirstName.get(player),playerSurname.get(player))))
            
                df1 = pd.DataFrame([[player,prob[0][0],pred[0],playerData_predictOnWeek['Label'][0],pointsIn_PredictForWeek[0]]],columns=['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
                results_LR=results_LR.append(df1)
    total = len(results_LR)
    results_actual1 = results_LR[results_LR['actualLabel'] == 1]
    results_actual0 = results_LR[results_LR['actualLabel'] == 0]  
#    acc = sum(results_actual1['predictedLabel'])/len(results_actual1)
    actual0 = len(results_actual0)
    actual1 = len(results_actual1)
    FP = sum(results_actual0['predictedLabel'])
    TN = actual0 - FP
    TP = sum(results_actual1['predictedLabel'])
    FN = actual1 - TP
    
    accuracy = 'Not enough data' if total == 0 else (TP+TN)/total
    specificity = 'Never scored below 5 till this week' if actual0 == 0 else TN/actual0 #When it's actually 0, how often does it predict 0?
    recall_senstivity = 'Never scored above 5 till this week' if actual1 == 0 else TP/actual1 #When it's actually 1, how often does it predict 1?
    precision = 'No 1s predicted' if sum(results_LR['predictedLabel']) ==0 else TP/sum(results_LR['predictedLabel']) #When it predicts yes, how often is it correct?
    playersInConsideration = sum(results_LR['predictedLabel'] == 1)
    playersPrunedOut = sum(results_LR['predictedLabel'] == 0)
    resultsOverSeveralWeeks_LR=resultsOverSeveralWeeks_LR.append(
            pd.DataFrame([[predictForWeek,accuracy,specificity,recall_senstivity,precision,
                           playersInConsideration,playersPrunedOut,playerPredictedToScore]],
        columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration']))
    
resultsOverSeveralWeeks_LR.to_csv('resultsOverSeveralWeeks_LR_'+str(pointForLabel)+'.csv')
t6 = time.time()
print('Time to Run LR '+str(t6-t5))
"""
Decision Tree
"""

t7 = time.time()
allPlayers = set(FPL16_Cleaned1['PlayerKey'])
weeks = set(FPL16_Cleaned1['Week'])
features = ['PointsLastRound','GoalsScored','CleanSheets','Assists']
resultsOverSeveralWeeks_DT = pd.DataFrame(columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration'])
weeks.remove(list(weeks)[0])
for predictForWeek in weeks:
    results_DT = pd.DataFrame(columns = ['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
    playerPredictedToScore = [tuple]
    for player in allPlayers:
        playerData = FPL16_Cleaned1[FPL16_Cleaned1['PlayerKey']==player]
        
        if predictForWeek in list(playerData['Week']):
            pointsIn_PredictForWeek = playerData[playerData['Week']==predictForWeek]['PointsLastRound']
        else:
            pointsIn_PredictForWeek = ['Did Not play']
            
        if predictForWeek-1 in list(playerData['Week']):
            playerData_predictOnWeek=playerData[playerData['Week']==predictForWeek-1]
        else:
            continue
        
        playerData = playerData[playerData['Week']<predictForWeek-1]
        if(len(playerData)!=0):
            clf = DecisionTreeClassifier(random_state=0)
            df = playerData[features]
            features_train = np.array(df.values,dtype=np.float)
            label_train = np.array(playerData['Label'],dtype=np.int)
            test = np.array(playerData_predictOnWeek[features].values,dtype=np.float)
            if len(set(label_train)) >1:
                clf = clf.fit(features_train, label_train)
                pred = clf.predict(test)
                prob = clf.predict_proba(test)
                if pred[0]==1:
                    playerPredictedToScore.append(tuple((player,playerFirstName.get(player),playerSurname.get(player))))
            
                df1 = pd.DataFrame([[player,prob[0][0],pred[0],playerData_predictOnWeek['Label'][0],pointsIn_PredictForWeek[0]]],columns=['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
                results_DT=results_DT.append(df1)
    total = len(results_DT)
    results_actual1 = results_DT[results_DT['actualLabel'] == 1]
    results_actual0 = results_DT[results_DT['actualLabel'] == 0]  
#    acc = sum(results_actual1['predictedLabel'])/len(results_actual1)
    actual0 = len(results_actual0)
    actual1 = len(results_actual1)
    FP = sum(results_actual0['predictedLabel'])
    TN = actual0 - FP
    TP = sum(results_actual1['predictedLabel'])
    FN = actual1 - TP
    
    accuracy = 'Not enough data' if total == 0 else (TP+TN)/total
    specificity = 'Never scored below 5 till this week' if actual0 == 0 else TN/actual0 #When it's actually 0, how often does it predict 0?
    recall_senstivity = 'Never scored above 5 till this week' if actual1 == 0 else TP/actual1 #When it's actually 1, how often does it predict 1?
    precision = 'No 1s predicted' if sum(results_DT['predictedLabel']) ==0 else TP/sum(results_DT['predictedLabel']) #When it predicts yes, how often is it correct?
    playersInConsideration = sum(results_DT['predictedLabel'] == 1)
    playersPrunedOut = sum(results_DT['predictedLabel'] == 0)
    resultsOverSeveralWeeks_DT=resultsOverSeveralWeeks_DT.append(
            pd.DataFrame([[predictForWeek,accuracy,specificity,recall_senstivity,precision,
                           playersInConsideration,playersPrunedOut,playerPredictedToScore]],
        columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration']))
    

resultsOverSeveralWeeks_DT.to_csv('resultsOverSeveralWeeks_DT_'+str(pointForLabel)+'.csv')
t8 = time.time()
print('Time to Run DT '+str(t8-t7))
"""
Ensembled Model
"""
t9 = time.time()
allPlayers = set(FPL16_Cleaned1['PlayerKey'])
weeks = set(FPL16_Cleaned1['Week'])
features = ['PointsLastRound','GoalsScored','CleanSheets','Assists']
resultsOverSeveralWeeks_SVM = pd.DataFrame(columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration'])
weeks.remove(list(weeks)[0])
for predictForWeek in weeks:
    results_SVM = pd.DataFrame(columns = ['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
    playerPredictedToScore = [tuple]
    for player in allPlayers:
        playerData = FPL16_Cleaned1[FPL16_Cleaned1['PlayerKey']==player]
        
        if predictForWeek in list(playerData['Week']):
            pointsIn_PredictForWeek = playerData[playerData['Week']==predictForWeek]['PointsLastRound']
        else:
            pointsIn_PredictForWeek = ['Did Not play']
            
        if predictForWeek-1 in list(playerData['Week']):
            playerData_predictOnWeek=playerData[playerData['Week']==predictForWeek-1]
        else:
            continue
        
        playerData = playerData[playerData['Week']<predictForWeek-1]
        if(len(playerData)!=0):
            clf = DecisionTreeClassifier(random_state=0)
            model = LogisticRegression()
            clf_NB = GaussianNB()
            
            df = playerData[features]
            features_train = np.array(df.values,dtype=np.float)
            label_train = np.array(playerData['Label'],dtype=np.int)
            test = np.array(playerData_predictOnWeek[features].values,dtype=np.float)
            if len(set(label_train)) >1:
                
                #Create Naive Bayes, Logistic Regression and Decision Tree Models
                clf = clf.fit(features_train, label_train)
                model = model.fit(features_train, label_train)
                clf_NB=clf_NB.fit(features_train, label_train)
                
                #Predict for Naive Bayes, Logistic Regression and Decision Tree Models
                prob_LR = model.predict_proba(features_train)
                prob_DT = clf.predict_proba(features_train)
                prob_NB = clf_NB.predict_proba(features_train)
                
                if np.isnan(prob_LR).any() or np.isnan(prob_DT).any() or np.isnan(prob_NB).any():
                    continue
                
                #New Features consisting of the probabilities from three different models
                newFeatures = np.matrix([prob_LR[:,0],prob_DT[:,0],prob_DT[:,0]]).T
                
                #Test vector consisting of the probabilities from the prev predictions
                probtest_LR = model.predict_proba(test)
                probtest_DT = clf.predict_proba(test)
                protestb_NB = clf_NB.predict_proba(test)
                newTest = np.matrix([probtest_LR[:,0],probtest_DT[:,0],protestb_NB[:,0]]).T
                
                #SVM model on top of the probabilities from three different models
                clf_SVM = svm.SVC()
                clf_SVM.fit(newFeatures, label_train)
                
                pred= clf_SVM.predict(newTest)
                prob = [[0]]#clf_SVM.predict_proba(newTest) #Commentted out because of some problem with predict_proba for SVM
                if pred[0]==1:
                    playerPredictedToScore.append(tuple((player,playerFirstName.get(player),playerSurname.get(player))))
            
                df1 = pd.DataFrame([[player,prob[0][0],pred[0],playerData_predictOnWeek['Label'][0],pointsIn_PredictForWeek[0]]],columns=['PlayerKey','prob','predictedLabel','actualLabel','pointsIn_PredictForWeek'])
                results_SVM=results_SVM.append(df1)
    total = len(results_SVM)
    results_actual1 = results_SVM[results_SVM['actualLabel'] == 1]
    results_actual0 = results_SVM[results_SVM['actualLabel'] == 0]  
#    acc = sum(results_actual1['predictedLabel'])/len(results_actual1)
    actual0 = len(results_actual0)
    actual1 = len(results_actual1)
    FP = sum(results_actual0['predictedLabel'])
    TN = actual0 - FP
    TP = sum(results_actual1['predictedLabel'])
    FN = actual1 - TP
    
    accuracy = 'Not enough data' if total == 0 else (TP+TN)/total
    specificity = 'Never scored below 5 till this week' if actual0 == 0 else TN/actual0 #When it's actually 0, how often does it predict 0?
    recall_senstivity = 'Never scored above 5 till this week' if actual1 == 0 else TP/actual1 #When it's actually 1, how often does it predict 1?
    precision = 'No 1s predicted' if sum(results_SVM['predictedLabel']) ==0 else TP/sum(results_SVM['predictedLabel']) #When it predicts yes, how often is it correct?
    playersInConsideration = sum(results_SVM['predictedLabel'] == 1)
    playersPrunedOut = sum(results_SVM['predictedLabel'] == 0)
    resultsOverSeveralWeeks_SVM=resultsOverSeveralWeeks_SVM.append(
            pd.DataFrame([[predictForWeek,accuracy,specificity,recall_senstivity,precision,
                           playersInConsideration,playersPrunedOut,playerPredictedToScore]],
        columns = ['Week','accuracy','specificity','recall_senstivity','precision','#playersInConsideration','#playersPrunedOut','playersInConsideration']))
    
resultsOverSeveralWeeks_SVM.to_csv('resultsOverSeveralWeeks_SVM_Ensembled_'+str(pointForLabel)+'.csv')
t10 = time.time()
print('Time to Run SVM(Ensembled Model) '+str(t10-t9))
print('Total Time '+str(t10-t1))


