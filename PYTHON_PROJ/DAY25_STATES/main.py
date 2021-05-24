# import pandas
# import csv

# # with open('weather_data.csv') as data_file:
# #     data = data_file.readlines()
# #     print(data)

# #OR...
# # #OPEN WEATHER CSV
# # with open('weather_data.csv') as data_file:
# #     temperatures = []
# #     # USE CSV IMPORT TO BREAK INTO READABLE LIST
# #     data = csv.reader(data_file)
# #     #GET TEMPERATURES
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# #OR...


# data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(data['temp'])

# data_dict = data.to_dict()
# # print(data_dict) 

# temp_list = data['temp'].to_list()
# # print(temp_list)

# # av_temp = round(sum(temp_list)/len(temp_list))
# av_temp = data['temp'].mean()
# # print(av_temp)

# max_temp = data['temp'].max()
# # print(max_temp)

# #GET DATA IN COLUMNS
# # print(data['temp'])
# # print(data.temp)

# #GET DATA IN ROWS
# # print(data[data.day == 'Monday'])
# max_head_day = data[data.temp == max_temp]
# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

#MAKE NEW DATAFRAME FROM SCRATCH
# data_dict = {
#     'student':['amy','James','Angela'],
#     'scores':[1,2,3]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
# print(data)
