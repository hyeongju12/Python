# # with open('data/weather_data.csv', 'r') as file:
# # 	contents = file.readlines()
# #
# # for content in contents:
# # 	print(content)
# #
#
#
# # import csv
# #
# # with open("data/weather_data.csv") as csv_file:
# # 	data = csv.reader(csv_file)
# # 	temperatures = []
# # 	for row in data:
# # 		if row[1] != "temp":
# # 			temperatures.append(row[1])
# #
# # print(temperatures)
#
# import pandas as pd
#
# data = pd.read_csv("data/weather_data.csv")
#
# temp_list = data["temp"].to_list()
#
# # print(max(temp_list))
# max_val = 0
#
# for temp in temp_list:
# 	if max_val < temp:
# 		max_val = temp
#
# print(max_val)
#
# print(data[data.day=='Monday'])
# print(data[data.temp==max(temp_list)])
# print(data[max(int((data.temp)])\

import pandas as pd

data = pd.read_csv("data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data[data.Location])
