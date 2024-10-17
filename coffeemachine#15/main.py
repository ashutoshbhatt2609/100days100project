from menu1 import *
water=resources["water"]
milk=resources["milk"]
coffee=resources["coffee"]
def choice():
    global power
    user=input("What would you like? (espresso/latte/cappuccino):")
    if user=="off":
        power="off"
    elif user=="report":
        for i in resources:
            print(i,resources.get(i))
    elif user=="espresso":
        requirements(user)
        functioning(user)
        print("Here is your coffee:- ☕")
    elif user=="latte":
        requirements(user)
        functioning(user)
    elif user=="cappuccino":
        requirements(user)
        functioning(user)
def functioning(user):
    detail=MENU[user]
    cost1=detail["cost"]
    print("Please insert coins.")
    money_got=cost()
    if  money_got<cost1:
        print("Insufficient money!!!!!, Money Refunded!!!!!")
    else:
        print(f"Remaining Change = {money_got-cost1}")

def requirements(coffee_name):
    global water,milk,coffee
    if coffee_name=="espresso":
        a=MENU.get(coffee_name)
        b=a.get("ingredients")
        c=a.get("cost")
        water_req=b["water"]
        coffee_req=b["coffee"]
        if water_req>water or coffee_req>coffee:
            print("Insufficient ingredients to make coffee.")
        else:
            water-=water_req
            coffee-=coffee_req
    else:
        a=MENU.get(coffee_name)
        b=a.get("ingredients")
        c=a.get("cost")
        water_req=b["water"]
        milk_req=b["milk"]
        coffee_req=b["coffee"]
        if water_req>water or milk_req>milk or coffee_req>coffee:
            print("Insufficient ingredients to make coffee.")
        else:
            water-=water_req
            milk-=milk_req
            coffee-=coffee_req
def cost():
    c1=int(input("How many pennies:-"))
    c2=int(input("How many dimes:-"))
    c3=int(input("How many nickels:-"))
    c4=int(input("How many quarters:-"))
    c1=0.01*c1
    c2=0.1*c2
    c3=0.05*c3
    c4=0.25*c4
    return (c1+c2+c3+c4)
power="on"
while power=="on":
    choice()




