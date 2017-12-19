import csv
import pandas as pd

varList1 = []
for i in range(1,712):
    varList1.append(i)
# with open('2014-2015_FPLData.csv', 'rU') as csvFileInput:
#     listOfDict1 = csv.DictReader(csvFileInput)
#     for dictionary in listOfDict1:
#         # print dictionary
#         varList1.append(dictionary['\xef\xbb\xbfName'])

df = pd.read_csv('2014-2015_FPLData.csv')
dw = df.groupby('ID').sum()
# print dw
dw['serialID'] = varList1
# print dw
print dw.shape

# print dw.shape


df1 = pd.read_csv('2014-2015_skillsData.csv', header=None )
# print df1
column_names = ['ID', 'Name', 'Team', 'Position', 'Availabilty', 'Selection', 'EA_INDEX', 'Price']
df2 = df1.iloc[1:]
# print df2
df2.columns = column_names
df2['serialID'] = varList1
print df2.shape


join_df = dw.merge(df2, on='serialID', how='left')

print join_df
join_df.to_csv("2014-15_FPLData.csv")
