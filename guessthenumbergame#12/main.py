from art import logo
import random
def compare():
    global i
    if guess>com_chosen:
        if (guess-com_chosen)<5:
            print("Close call , guess low!!")
        else:
            print("Too high, guess again!!")
    elif guess<com_chosen:
        if (com_chosen-guess)<5:
            print("Close call , guess high!!")
        else:
            print("Too low, guess again!!")
    else:
        print("You Guessed the correct number.")
        i=0
        
         
    
def easy():
    global i
    i=10
    global guess
    while i>0:
            print(f"You have {i} attempts remaining to guess the number.")
            guess=int(input("Make a guess:"))
            i-=1
            compare()
def hard():
    global i
    i=5
    global guess
    while i>0:
            print(f"You have {i} attempts remaining to guess the number.")
            guess=int(input("Make a guess:"))
            i-=1
            compare()


     
     
def game():
    print(logo)
    print("Welcome to the number guessing game!!!!")
    print("I'm thinking of a number between 1 and 100.")
    dif=input("Choose a difficulty. Type 'easy' or 'hard':-")
    global com_chosen
    com_chosen=random.randint(1,100)
    if dif=="easy":
        easy()
    elif dif=="hard":
        hard()
game()

            
