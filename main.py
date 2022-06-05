# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "student": ["Aaa", "Bbb", "Ccc"],
#     "score": [78, 87, 55]
# }
#
# data = pd.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
