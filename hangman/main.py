import random
from words import word
from art import logo 
from art import stages
def result(l,a):
    global life
    if l>=1:
        if "_" not in a:
            print("You won!!!!!!!")
            life=0
    elif l<=0:
        print("You Loose!!!!!\nWord is:-",choosen_word)



def answer(i,s):
    global ans
    ans.pop(s)
    ans.insert(s,i)
def game():
    global life
    s=-1
    for i in choosen_word:
        s+=1
        if i == guess:
            answer(i,s)
        
    if guess not  in choosen_word:
        life-=1
    print(ans,"Life remaining:-",life,stages[life]) 
    result(life,ans) 
print(logo) 
life=6
choosen_word=random.choice(word).lower()
ans=[]
len_chosen_word=len(choosen_word)
for j in range(len_chosen_word):
    ans.extend("_")
while life>=1:
    guess=input("Enter your guess:-\n")
    game()

