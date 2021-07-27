from flask import request, redirect, url_for, render_template, flash
from flaskr import app
import random
import csv


@app.route('/')
def show_menus():
    return render_template('show_menus.html')

@app.route('/1000', methods=['GET'])
def get_1000():
    money = 1000
    return(get_menus(money))

@app.route('/1500', methods=['GET'])
def get_1500():
    money = 1500
    return(get_menus(money))

@app.route('/2000', methods=['GET'])
def get_2000():
    money = 2000
    return(get_menus(money))

@app.route('/balance', methods=['GET'])
def balance():
    menus = []
    text = "コメダ珈琲バランスガチャを回したよ！" + "\n" + "\n"
    calories = 0
    budget = 0
    dish = ["meal", "drink"]

    # import csv
    with open ('./flaskr/komeda.csv', "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        list_of_rows = list(csv_reader)
    # add meal and drink
    while len(menus) < 2:
        candidate = random.choice(list_of_rows)
        if candidate[2] != dish[len(menus)]:
            continue
        menus.append(candidate)
        text += str(candidate[1]) + "\n"
        budget += int(candidate[4])
        calories += int(candidate[5])
    # add dessert
    while len(menus) < 3:
        candidate = random.choice(list_of_rows)
        if candidate[2] == "side" and candidate[3] == "dessert":
            menus.append(candidate)
            text += str(candidate[1]) + "\n"
            budget += int(candidate[4])
            calories += int(candidate[5])
        else:
            continue

    # tweet result
    text += "\n"
    text += "計 " + str(budget) + "円 " + str(calories) + "kcal" + "\n" + "#コメダ珈琲ガチャ" + "\n" 

    return render_template('show_menus.html', menus=menus, budget=budget, calories=calories, text=text)


def get_menus(money):
    # params
    menus = []
    text = "コメダ珈琲" + str(money) + "円ガチャを回したよ！" + "\n" + "\n"
    budget = money
    calories = 0

    # import csv
    with open ('./flaskr/komeda.csv', "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        list_of_rows = list(csv_reader)

    while budget > 240:
        candidate = random.choice(list_of_rows)
        if int(candidate[4]) > budget:
            continue
        menus.append(candidate)
        text += str(candidate[1]) + "\n"
        budget -= int(candidate[4])
        calories += int(candidate[5])

    budget = money - budget

    # tweet result
    text += "\n"
    text += "計 " + str(budget) + "円 " + str(calories) + "kcal" + "\n" + "#コメダ珈琲ガチャ" + "\n" 

    return render_template('show_menus.html', menus=menus, budget=budget, calories=calories, text=text)