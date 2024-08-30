print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
a=input('You\'re at a cross road. Where do you want to go? Type "Left" or "Right"\n')
if a=="Right":
    print("You fell into a hole, Game Over!!!!!")
elif a=="Left":
    b=input("You came to a lake . There is a island in the middle. Type \"Wait\" to wait for boat. Type \"Swim\" to swim across.\n")
    if b=="Swim":
        print("Game Over!!!!!")
    elif b=="Wait":
        c=input("You have to get into any of the three boat. Type \"Red\",\"Blue\",\"Yellow\" to select the boat\n")
        if c=="Yellow":
            print("You Win!!!!!!!!!!") 
        elif c=="Red":
            print("""Burned by fire.\nGame Over.""")
        elif c=="Blue":
            print("""Eaten by beasts.\nGame Over""")

else:
    print("Game Over!!!!!")

          
