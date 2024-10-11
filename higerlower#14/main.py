import random
from art import *
from gamedata import data
count=0
def selection():
    a1=random.choice(data)
    name1=a1["name"]
    descri1=a1["description"]
    foll1=a1["follower_count"]
    country1=a1["country"]
    print(f"Compare A:- {name1},{descri1},{country1}")
    print(vs)
    a2=random.choice(data)
    while a1==a2:
        a2=a2=random.choice(data)
    name2=a2["name"]
    descri2=a2["description"]
    foll2=a2["follower_count"]
    country2=a2["country"]
    print(f"Compare B:- {name2},{descri2},{country2} ",end=" ")
    ans=input("Type \"A\" or \"B\" ?:-")
    compare(foll1,foll2,ans) 
def compare(f1,f2,ans):
    global count
    
    if ans=="A" and f1>f2:
        count+=1
        print(f"You're right! Current score:{count}")
        selection()
    elif ans=="B" and f2>f1:
        count+=1
        print(f"You're right! Current score:{count}")
        selection()
    else:
        print(f"Sorry, that's wrong. Final score: {count}")

def game():
    print(logo)
selection()