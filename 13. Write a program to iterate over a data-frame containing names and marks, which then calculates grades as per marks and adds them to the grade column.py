import pandas as pd
import numpy as np
names = pd.Series (['Abhinav', 'Aman', 'Sunil', 'Tejas', 'Manon'])
marks = pd. Series ([61, 75.0, 95, 89, 73.6])
Stud = { 'Name': names, 'Marks': marks }
df1 = pd.DataFrame (Stud, columns = ['Name', 'Marks'])
df1['Grade'] = np.NaN
print ("Initial values in dataframe")
print (df1)

for (col, colSeries) in df1.iteritems():
    length = len(colSeries)
    if col == 'Marks':
        lstMrks = []
        for row in range (length) :
            mrks = colSeries [row]
            if mrks >= 90 :
                lstMrks.append('A+')
            elif mrks >= 70 :
                lstMrks.append('A')
            elif mrks >= 60 :
                lstMrks.append('B')
            elif mrks >= 50 :
                lstMrks.append('C')
            elif mrks >= 40:
                lstMrks.append('D')
            else:
                lstMrks.append('F')

df1['Grade'] = lstMrks
print("\n Dataframe after calculating grades")
print (df1)
