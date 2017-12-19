import csv
import os
import numpy as np
from sklearn.naive_bayes import GaussianNB
import xlsxwriter as xw
from sklearn.metrics import confusion_matrix

import warnings

file_path = os.currdir
files = os.listdir(file_path)
files_txt = [i for i in files if i.endswith('.csv')]

week = input('Enter the week: ')

data = {}
label = {}

output_data = []
matrix_data = []

warnings.filterwarnings("ignore")

max_week = 5
for f in files_txt:
    weeknum = int(f[8:9]) if len(f) == 13 else int(f[8:10])
    if weeknum > max_week:
        max_week = weeknum
    myfile = file_path + '/' + f
    ff = open(myfile)
    reader = csv.reader(ff)
    temp = 1
    for row in reader:
        if temp>1:
            if row[0] != '' and row[1] != '':
                data.setdefault(row[0]+row[1], []).append(list([weeknum]) + list([int(row[5])]) + list([int(row[12])]) + list([int(row[13])]) + list([int(row[17])]) + list([int(row[26])]) + list([int(row[28])]) + list([int(row[30])]) + list([int(row[37])]) + list([int(row[39])]) + list([int(row[42])]) + list([int(row[43])]))
                label.setdefault(row[0]+row[1], []).append(list([weeknum]) + list([int(row[38])]))
            elif row[0] == '' and row[1] != '':
                data.setdefault(row[1], []).append(list([weeknum]) + list([int(row[5])]) + list([int(row[12])]) + list([int(row[13])]) + list([int(row[17])]) + list([int(row[26])]) + list([int(row[28])]) + list([int(row[30])]) + list([int(row[37])]) + list([int(row[39])]) + list([int(row[42])]) + list([int(row[43])]))
                label.setdefault(row[1], []).append(list([weeknum]) + list([int(row[38])]))
            elif row[1] == '' and row[0] != '':
                data.setdefault(row[0], []).append(list([weeknum]) + list([int(row[5])]) + list([int(row[12])]) + list([int(row[13])]) + list([int(row[17])]) + list([int(row[26])]) + list([int(row[28])]) + list([int(row[30])]) + list([int(row[37])]) + list([int(row[39])]) + list([int(row[42])]) + list([int(row[43])]))
                label.setdefault(row[0], []).append(list([weeknum]) + list([int(row[38])]))
        temp+=1

for k in data:
    data[k].sort(key = lambda row: (row[0]))
    label[k].sort(key = lambda row: (row[0]))

accuracy = 0
for k in data:
    i = 0
    while i<len(data[k]) - 1:
        data[k][i][1] = data[k][i+1][1]
        if label[k][i+1][1] - label[k][i][1] <= 1:
            label[k][i][1] = label[k][i+1][1] - label[k][i][1]
        else:
            label[k][i][1] = 1
        j=2
        while j<len(data[k][i]):
            if j==2:
                data[k][i + 1][j] = data[k][i + 1][j] - data[k][i][j]
            j = j+1
        i+=1
    data[k] = data[k][1:len(data[k]) - 1]
    label[k] = label[k][1:len(label[k]) - 1]

#week = 7
while week <= len(files_txt) + 4:
    data_temp = data
    label_temp = label
    accuracy = 0
    predicted_output = []
    expected_output = []
    for k in data_temp:
        w = 6
        data_train = []
        label_train = []
        while w<week-1:
            n = 0
            while n<len(data_temp[k]):
                if w == data_temp[k][n][0]:
                    data_train.append(data_temp[k][n][1:])
                    label_train.append(label[k][n][1:])
                n = n+1
            w = w+1

        w = week-1
        data_test = []
        label_test = []

        n = 0
        while n < len(data_temp[k]):
            if w == data_temp[k][n][0]:
                data_test.append(data_temp[k][n][1:])
                label_test.append(label[k][n][1:])
            n = n + 1

        if len(data_train)>0 and len(data_test)>0:

            X = np.array(data_train)
            Y = np.array(label_train)
            X_test = np.array(data_test)
            Y_test = np.array(label_test)

            clf = GaussianNB()
            clf.fit(X, Y)
            res = clf.predict(X_test)

            expected_output.append(label_test[0])
            predicted_output.append(res[0])

            player_data = []
            player_data.append(k)
            player_data.append(week)
            player_data.append(res[0])
            output_data.append(player_data)

    cm = confusion_matrix(expected_output, predicted_output)
    if len(cm)!=0:
        tn = float(cm[0][0])
        fp = float(cm[0][1])
        fn = float(cm[1][0])
        tp = float(cm[1][1])
        # sensitivity
        if tp+fn!=0:
            TPR = float(tp / (tp + fn))
        else:
            TPR = 0

        # specificity
        if tn+fp != 0:
            TNR = float(tn / (tn + fp))
        else:
            TNR = 0

        # precision
        if tp+fp != 0:
            PPV = float(tp / (tp + fp))
        else:
            PPV = 0

        # Overall accuracy
        if tp+fp+fn+tn != 0:
            ACC = float((tp + tn) / (tp + fp + fn + tn))
        else:
            ACC = 0

        stats = []
        stats.append(week)
        stats.append(TPR)
        stats.append(TNR)
        stats.append(PPV)
        stats.append(ACC)
        matrix_data.append(stats)

    week += 1

wb = xw.Workbook("Gaussian_Naive_Bayes_Output.xlsx")
format = wb.add_format()
format.set_bold()
format.set_font_color('#2F75B5')
format.set_font('Calibri')
format.set_font_size('16')

ws1 = wb.add_worksheet()
ws1.hide_gridlines(2)
ws1.set_column('A:N',10)
ws1.write(1,0,'Guassian Naive Bayes Results:',format)
cell_range1 = xw.utility.xl_range(3,0,3+len(matrix_data),4)
c1 = [{'header': 'Week'},{'header': 'Sensitivity'},{'header': 'Specificity'},{'header': 'Precision'},{'header': 'Accuarcy'},]
ws1.add_table(cell_range1,{'data':matrix_data, 'columns':c1,'style':'Table Style Light 9','autofilter':True})

ws2 = wb.add_worksheet()
ws2.hide_gridlines(2)
ws2.set_column('A:N',10)
ws2.write(1,0,'Gaussian Naive Bayes Predictions:',format)
cell_range2 = xw.utility.xl_range(3,0,3+len(output_data),2)
c2 = [{'header': 'PlayerName'},{'header': 'Week'},{'header': 'Dream Team'},]
ws2.add_table(cell_range2,{'data':output_data, 'columns':c2,'style':'Table Style Light 9','autofilter':True})

wb.close()
