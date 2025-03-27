import csv
import pandas as pd
# data =  pd.read_csv("csv-files/weather_data.csv")
# average = 0 
# for temp in data["temp"]:
#     average += temp
# print(average/len(data["temp"]))
# print(data[data["temp"] == data["temp"].max()])
# monday = data[data.day == 'Monday']
# fahrenhei = monday.temp[0] *9/5 


data = pd.read_csv("csv-files/squirerel_data.csv")

sum_fur = 0


gray_fur = len(data[data["Primary Fur Color"]== "Gray"])

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_fur = len(data[data["Primary Fur Color"] == "black"])

new_data = {
    "Fur Color" : ["gray", "cinnamon", "black"],
    "count" : [gray_fur, cinnamon, black_fur]

}

df = pd.DataFrame(new_data)

df.to_csv("new.csv")





