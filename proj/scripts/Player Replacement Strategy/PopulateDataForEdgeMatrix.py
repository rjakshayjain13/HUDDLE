import csv
import pandas as pd
import numpy as np
team = "ARS"
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
f11 = []
f12 = []
f13 = []
with open('2015-16_FPLData.csv', 'rU') as csvFileInput:
    listOfDict1 = csv.DictReader(csvFileInput)
    for dictionary in listOfDict1:
        #print dictionary
        if dictionary['Team'] == team:
            f1.append("2015-16")
            f2.append(dictionary['Team'])
            f3.append(dictionary['Pos'])
            f4.append(dictionary['\xef\xbb\xbfName'])
            f5.append(dictionary['Points'])
            f6.append(dictionary['Goals'])
            f7.append(dictionary['Assists'])
            f8.append(dictionary['Minutes'])
            f9.append(dictionary['Reds'])
            f10.append(dictionary['Yellows'])
            f11.append(dictionary['Saves'])
            f12.append(dictionary['Bonus'])
            f13.append(dictionary['CS'])

with open('2016-17_FPLData.csv', 'rU') as csvFileInput:
    listOfDict1 = csv.DictReader(csvFileInput)
    for dictionary in listOfDict1:
        if dictionary['Team'] == team:
            f1.append("2016-17")
            f2.append(dictionary['Team'])
            f3.append(dictionary['Pos'])
            f4.append(dictionary['\xef\xbb\xbfName'])
            f5.append(dictionary['Points'])
            f6.append(dictionary['Goals'])
            f7.append(dictionary['Assists'])
            f8.append(dictionary['Minutes'])
            f9.append(dictionary['Reds'])
            f10.append(dictionary['Yellows'])
            f11.append(dictionary['Saves'])
            f12.append(dictionary['Bonus'])
            f13.append(dictionary['CS'])

print f1

csvFileInput.close();

with open('2014-15_FPLData.csv', 'rU') as csvFileInput:
    listOfDict1 = csv.DictReader(csvFileInput)
    for dictionary in listOfDict1:
        if dictionary['Team'] == team:
            f1.append("2014-15")
            f2.append(dictionary['Team'])
            f3.append(dictionary['Position'])
            f4.append(dictionary['Name'])
            f5.append(dictionary['Points'])
            f6.append(dictionary['Goals'])
            f7.append(dictionary['Assists'])
            f8.append(dictionary['Mins'])
            f9.append(dictionary['Red_Cards'])
            f10.append(dictionary['Yellow_Cards'])
            f11.append(dictionary['Saves'])
            f12.append(dictionary['Bonus'])
            f13.append(dictionary['Clean_Sheets'])

print f1

csvFileInput.close();

df = pd.DataFrame({
    'Season': f1,
    'Team': f2,
    'Pos': f3,
    'Name': f4,
    'Points': f5,
    'Goals': f6,
    'Assists': f7,
    'Minutes': f8,
    'Reds_Cards': f9,
    'Yellow_Cards': f10,
    'Saves': f11,
    'Bonus': f12,
    'Clean_Sheets': f12

})
df.to_csv('DataForEdgeMatrix.csv', index=False)
