import pandas

csv = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_rows = csv[csv["Primary Fur Color"] == "Gray"]
grey_fur = grey_rows["Primary Fur Color"].count()

cinnamon_rows = csv[csv["Primary Fur Color"] == "Cinnamon"]
cinnamon_fur = cinnamon_rows["Primary Fur Color"].count()

black_rows = csv[csv["Primary Fur Color"] == "Black"]
black_fur = black_rows["Primary Fur Color"].count()

fur_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [grey_fur, cinnamon_fur, black_fur]
}
# print(fur_dict)
fur_data_frame = pandas.DataFrame(fur_dict)
fur_data_frame.to_csv("./squirrel_count.csv")