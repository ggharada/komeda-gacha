import csv
import random

menus = []
text = "コメダ珈琲バランスガチャを回したよ！" + "\n" + "\n"
calories = 0
budget = 0
dish = ["meal", "drink"]

with open ('komeda.csv', "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_rows = list(csv_reader)
#add meal and drink
while len(menus) < 2:
    candidate = random.choice(list_of_rows)
    if candidate[2] != dish[len(menus)]:
        continue
    menus.append(candidate)
    text += str(candidate[1]) + "\n"
    budget += int(candidate[4])
    calories += int(candidate[5])
#add dessert
while len(menus) < 3:
    candidate = random.choice(list_of_rows)
    if candidate[3] != "dessert":
        continue
    menus.append(candidate)
    text += str(candidate[1]) + "\n"
    budget += int(candidate[4])
    calories += int(candidate[5])
print(menus)