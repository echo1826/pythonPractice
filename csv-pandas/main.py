with open("./weather_data.csv") as file:
    data = file.readlines()
    print(data)

import csv

with open("./weather_data.csv") as file:
    # csv.reader() will read the csv file provided as argument and return a reader object
    data = csv.reader(file)
    # reader object will contain the csv data in a list of rows for each row entry
    print(data)
    temperatures = []
    next(data)
    for row in data:
        temperatures.append(int(row[1]))
    print(temperatures)

import pandas

# formats it more like a table
# takes the first row of csv as the headers of the table and everything underneath it will be the data itself
csv = pandas.read_csv("./weather_data.csv")
# data returns back a data type called DataFrame
# The two primary data structures of pandas, Series (1-dimensional) and DataFrame(2-dimensional)
# a DataFrame is the equivalent of the whole table/spreadsheet doc
print(type(csv))

# a single "column" of the table is called a Series equivalent to a list in python
print(csv["temp"])