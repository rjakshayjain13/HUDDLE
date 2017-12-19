import csv
import pandas as pd
team = "ARS"
varList1 = []
with open('2015-16_FPLData.csv', 'rU') as csvFileInput:
    listOfDict1 = csv.DictReader(csvFileInput)
    for dictionary in listOfDict1:
        if dictionary['Team'] == team:
            varList1.append(dictionary['\xef\xbb\xbfName'])

varList2 = []
with open('2016-17_FPLData.csv', 'rU') as csvFileInput:
    listOfDict2 = csv.DictReader(csvFileInput)
    for dictionary in listOfDict2:
        if dictionary['Team'] == team:
            varList2.append((dictionary['\xef\xbb\xbfName']))


varList3 = []
with open('2014-15_FPLData.csv', 'rU') as csvFileInput1:
    listOfDict3 = csv.DictReader(csvFileInput1)
    for dictionary in listOfDict3:
        if dictionary['Team'] == team:
            varList3.append((dictionary['Name']))

commonPlayers = set(varList1) & set(varList2) & set(varList3)
count = 0
listOfPlayers = []
for i in commonPlayers:
    # if(count <= 20):     # currently only keeping it to 20 players
    #     count+=1
    #     listOfPlayers.append(i)
    listOfPlayers.append(i)
print listOfPlayers
print " The length of list of players common in the seasons : " + str(len(listOfPlayers))
map = {}
with open('DataForEdgeMatrix.csv', 'rb') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in fileReader:
        # value = row[10] + ":" + row[11] + ":" + row[7]   ## for season : team : position
        value = row[10] + ":" + row[11]  ## for season : team
        key = row[5]
        if key in map:
            map[key].append(value)
        else:
            ls = []
            ls.append(value)
            map[key] = ls

print map

map1 = {}
with open('DataForEdgeMatrix.csv', 'rb') as csvfile:
    fileReader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in fileReader:
        # value = row[10] + ":" + row[11] + ":" + row[7]   ## for season : team : position
        value = row[10] + ":" + row[7]  ## for season : position
        key = row[5]
        if key in map1:
            map1[key].append(value)
        else:
            ls = []
            ls.append(value)
            map1[key] = ls

print map1


f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []
f7 = []
f8 = []
f9 = []
f10 = []
with open('DataForEdgeMatrix.csv', 'rU') as csvFileInput:
    listOfDict1 = csv.DictReader(csvFileInput)
    for dictionary in listOfDict1:
        f1.append(dictionary["Assists"])
        f2.append(dictionary['Bonus'])
        f3.append(dictionary['Clean_Sheets'])
        f4.append(dictionary['Goals'])
        f5.append(dictionary['Minutes'])
        f6.append(dictionary['Points'])
        f7.append(dictionary['Reds_Cards'])
        f8.append(dictionary['Saves'])
        f9.append(dictionary['Yellow_Cards'])

print f1

csvFileInput.close();

df = pd.DataFrame({' ': f1,'  ': f2,'   ': f3,'    ': f4,'     ' :f5,'      ': f6,'       ':f7,'        ':f8,'         ':f9})
df.to_csv('SkillsSet.csv',header = False, encoding='utf-8', index=False)

for i in range(0, len(listOfPlayers)):
    print str(i)+  " : " + listOfPlayers[i]

file = open('matrixForFPL.txt', 'wb')
for p1 in listOfPlayers:
    output = ""
    for p2 in listOfPlayers:
        if (p1 == p2):
            output = output + str(len(map[p1]) + len(map1[p1])) + ","
        else:
            p1History = map[p1]
            p2History = map[p2]
            p3History = map1[p1]
            p4History = map1[p2]
            output = output + str(len(list(set(p1History).intersection(set(p2History)))) + len(
                list(set(p3History).intersection(set(p4History))))) + ","
            # print output
    output = output[0: len(output) - 1]
    file.write(output + '\n')

file.close()
