from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models import Menu
import random


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

    #add meal and drink
    for i in range(2):
        candidate = db.session.query(Menu).filter(Menu.category == dish[i]).all()
        food = random.choice(candidate)
        menus.append(food)
        text += str(food.name) + "\n"
        budget += int(food.price)
        calories += int(food.calories)

    #add dessert
    candidate = db.session.query(Menu).filter(Menu.type == "dessert", Menu.category == "side").all()
    food = random.choice(candidate)
    menus.append(food)
    text += str(food.name) + "\n"
    budget += int(food.price)
    calories += int(food.calories)

    # tweet result
    text += "\n"
    text += "計 " + str(budget) + "円 " + str(calories) + "kcal" + "\n" + "\n"

    return render_template('show_menus.html', menus=menus, budget=budget, calories=calories, text=text)


def get_menus(money):
    # params
    menus = []
    text = "コメダ珈琲" + str(money) + "円ガチャを回したよ！" + "\n" + "\n"
    budget = money
    calories = 0

    # select first food
    while not menus:
        rand = random.randrange(
            0, db.session.query(Menu.id).count()) + 1
        menus = db.session.query(Menu).filter(
            Menu.id == rand, Menu.price <= budget).all()

    # calc
    budget -= int(menus[0].price)
    calories += int(menus[0].calories)

    # add text for tweet
    text += str(menus[0].name) + "\n"

    while budget > 0:

        # avalable food candidate
        candidate = db.session.query(Menu).filter(Menu.price <= budget).all()

        # no candidate break
        if not candidate:
            break

        # select food
        food = random.choice(candidate)

        #被り防止
        if food in menus:
            break

        # add to list
        menus.append(food)

        # add text for tweet
        text += str(food.name) + "\n"

        # calc
        budget -= int(food.price)
        calories += int(food.calories)

    budget = money - budget

    # tweet result
    text += "\n"
    text += "計 " + str(budget) + "円 " + str(calories) + "kcal" + "\n" + "\n"

    return render_template('show_menus.html', menus=menus, budget=budget, calories=calories, text=text)