menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
import os
from time import sleep
#  TODO  type of coffee
def coffee(coffee_type):


    amt_water =  ((menu[coffee_type])["ingredients"])["water"]
    amt_milk = ((menu[coffee_type])["ingredients"])["milk"]
    amt_coffee = ((menu[coffee_type])["ingredients"])["coffee"]
    cost_coffee = (menu[coffee_type])["cost"]

    return [amt_water, amt_milk, amt_coffee, cost_coffee]


#  TODO  cost calculation
def cost(y):
    print("Please insert coins.")
    quarters = input("How many quarters?")
    dimes = input("How many dimes?")
    nickles = input(f"How many nickes?")
    pennies = input(f"How many pennies?")

    Total_cost = (float(quarters)*0.25 + float(dimes)*0.10 +  float(nickles)*0.05 + float(pennies)*0.01) - y
    return  print(f"Your change is: {round(Total_cost, 2)}")

#  TODO: Print report
def rep(x):
    global resources
    sub_resource = coffee(x)

    resources["water"] -= sub_resource[0]
    resources["milk"] -= sub_resource[1]
    resources["coffee"] -= sub_resource[2]

    return sub_resource[3]
#  TODO: Actual Machine
def machine():
    coffee_type = input("What would you like? espresso/latte/cappuccino: ").lower()
    if coffee_type == "report":
        w = resources
        for l in w:
            print(f"{l} = {w[l]}")
        sleep(2)
        os.system('cls')
        machine()
    if resources["water"] < ((menu[coffee_type])["ingredients"])["water"]:
        print("not enough water")
        quit()
    if resources["milk"] < ((menu[coffee_type])["ingredients"])["milk"]:
        print("not enough milk")
        quit()
    if resources["coffee"] < ((menu[coffee_type])["ingredients"])["coffee"]:
        print("not enough coffee")
        quit()
    if coffee_type == "latte":
        v = rep(coffee_type)
        cost(v)
        print(f"Here is your {coffee_type} ☕ Enjoy! \n")
        sleep(2)
        os.system('cls')
        machine()
    if coffee_type == "espresso":
        v = rep(coffee_type)
        cost(v)
        print(f"Here is your {coffee_type} ☕ Enjoy! \n")
        sleep(2)
        os.system('cls')
        machine()
    if coffee_type == "cappucino":
        v = rep(coffee_type)
        cost(v)
        print(f"Here is your {coffee_type} ☕ Enjoy! \n")
        sleep(2)
        os.system('cls')
        machine()

machine()
