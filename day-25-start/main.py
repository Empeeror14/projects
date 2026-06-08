# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open ("weather_data.csv") as data_file:
#     data =csv.reader(data_file)
#     temperature = []
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temperature.append(temp)
#     print(temperature)
        
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

max_temp = data["temp"].max()
print(data[data.temp == max_temp])
