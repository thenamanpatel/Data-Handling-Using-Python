import pandas as pd 
# initialize list of lists
data = [['CAR','Maruti',1000000],['AC','Hitachi',55000],['AIRCOLLER','Bajaj',12000],
['WASHING MACHINE','LG',15000],['CAR','Ford',7000000],['AC','SAMSUNG',45000],['AIRCOLLER','Symphony',20000],['WASHING MACHINE','Wirlpool',25000]]
Col=['itemcat','itemname','expenditure']
# Create the pandas DataFrame
qrtsales = pd.DataFrame(data,columns=Col)
# print dataframe. 
print (qrtsales)
qs=qrtsales.groupby('itemcat') 
print('Result after Filtering Dataframe') 
print(qs['itemcat','expenditure'].sum())
