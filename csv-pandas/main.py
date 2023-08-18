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

# pandas has multiple methods that can convert a DataFrame to any kind of data type/format: https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion
data = csv.to_dict()
print(data)

# # series also has multiple methods to be converted to a different data type
temp_list = csv["temp"].to_list()
print(temp_list)

# not using built in methods
total_temp = 0
for temp in temp_list:
    total_temp += temp
avg_temp = total_temp/len(temp_list)
print(int(avg_temp))

# built in methods solution
avg_temp = sum(temp_list)/len(temp_list)
print(int(avg_temp))

# pandas methods solution
pandas_avg = csv["temp"].mean()
print(int(pandas_avg))

# # maximum value in series
max_temp = csv["temp"].max()
print(max_temp)

# # can use dot notation to access different columns
print(csv.temp)

# # get entire row of data with pandas
row = csv[csv.day == "Monday"]
print(row)

# get row of data where temp is max
max_temp_row = csv[csv.temp == csv.temp.max()]
print(max_temp_row)

# get monday's temp and convert to farenheit
monday = csv[csv.day == "Monday"]
monday.temp = (monday.temp * 9/5) + 32
print(monday.temp)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dict)
# can create a csv file from a dataframe with pandas
data_frame.to_csv("./new_data.csv")