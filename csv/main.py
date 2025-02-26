import csv 
import pandas
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)

#     for row in data:
#         print(row)

data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(type(data["day"]))
# print(data)
# print(data.day)

# data_list = data.day.to_list()
# print(data_list)
# print(len(data_list))
# print(data.to_dict())
temp_data = data.temp 
print(data)
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
# print(temp_data.max())
# print(temp_data.mean())

data_dict = {
    "names" : ["Hitesh", "Monali", "Abhimanyu"],
    "age" : [41, 38, 12]
}

data = pandas.DataFrame(data_dict)

data.to_csv("family_data.csv")