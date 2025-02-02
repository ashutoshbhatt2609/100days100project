import csv
with open("DAy-25\weather_data.csv,'r") as data_file:
    data=csv.reader(data_file)
    for row in data:
        print(row)