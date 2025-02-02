import csv
with open("DAy-25\weather_data.csv",'r') as data_file:
    data= csv.reader(data_file)
    date=[]
    temp=[]
    weather=[]
    for row in data:
        if row[0]!='day':
            date.append(row[0])
        if row[1]!='temp':
            temp.append(int(row[1]))
        if row[0]!='condition':
            weather.append(row[2])


import pandas
data2=pandas.read_csv("DAy-25\weather_data.csv")
print(data2)
print(data2['temp'])
print(data2['day'])
print(data2['condition'])