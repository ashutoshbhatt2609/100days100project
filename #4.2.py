r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
comp=[r,s,p]
a=input("Enter your choice in rock paper scissors(r,s,p):-\n").capitalize()
c=random.choice(comp)
if c==r :
    if a=="P":
        print("Computer choice:-\n",c)
        print("Your choice:-\n",p)
        print("You Win!")
    elif a=="R":
        print("Computer choice:-\n",c)
        print("Your choice:-\n",r)
        print("Draw!") 
    else:
        print("Computer choice:-\n",c)
        print("Your choice:-\n",s) 
        print("You loose!")   

elif c==s :
    if a=="R":
        print("Computer choice:-\n",c)
        print("Your choice:-\n",r)
        print("You Win!")
    elif a=="P":
        print("Computer choice:-\n",c)
        print("Your choice:-\n",p)
        print("You loose!")  
    else:
        print("Computer choice:-\n",c)
        print("Your choice:-\n",s) 
        print("Draw!") 
elif c==p :
    if a=="S":
        print("Computer choice:-\n",c)
        print("Your choice:-\n",s)
        print("You Win!")
    elif a=="P":
        print("Computer choice:-\n",c)
        print("Your choice:-\n",p)
        print("Draw!") 
    else:
        print("Computer choice:-\n",c)
        print("Your choice:-\n",r) 
        print("You loose!") 
