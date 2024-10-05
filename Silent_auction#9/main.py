from art import logo
print(logo)
import os
record={}
ans="Yes"
highest=0
while ans=="Yes":
    name=input("What is your name:-")
    price=int(input("What is your bid:- $"))
    record[name]=price
    ans=input("Enter 'Yes' you have to add another bider or else enter 'No':-")
    if ans=="Yes":
        os.system('clear') 
    else:
        for bider in record:
            bid_amount=record[bider]
            if bid_amount>highest:
                highest=bid_amount
                winner=bider
        print(f"The winner of the auction is {winner}")




