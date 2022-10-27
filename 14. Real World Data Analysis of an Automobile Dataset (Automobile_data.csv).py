# a.	From the given dataset print the first and last five rows

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df.head(5)

df = pd.read_csv("Automobile_data.csv")
df.tail(5)

print(df)



# b.	Clean the dataset and update the CSV file

import pandas as pd
df = pd.read_csv("Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]}
)
print (df)

df.to_csv("Automobile_data.csv")



# c.	Find the most expensive car company name

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
print(df)



# d.	Print All Toyota Cars details

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)


# e.	Count total cars per company
import pandas as pd
df = pd.read_csv("Automobile_data.csv")
countdf = df['company'].value_counts()
print(countdf)



# f.	Find each company’s highest price car

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
print(priceDf)



# g.	Find the average mileage of each car making company

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
print(mileageDf)



# h.	Sort all cars by Price column

import pandas as pd
carsDf = pd.read_csv("Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf)



# i.	Concatenate two data frames

import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)

carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
print(carsDf)



# j.	Merge two data frames

import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
print(carsDf)
