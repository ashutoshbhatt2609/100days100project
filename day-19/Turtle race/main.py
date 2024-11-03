import turtle as t
import random as r
race_is_on=False
srn=t.Screen()
srn.setup(500,450)
user_bet=srn.textinput(title="Make your bet",prompt="Which turtle will win th race? Enter a code:")
print(user_bet)
color=['red','orange','black','blue','green']
turtles=[]
for i in range(5):
    new_turtle=t.Turtle(shape='turtle')
    turtles.append(new_turtle)
    new_turtle.color(color[i])
    new_turtle.pu()
    new_turtle.setposition(-230, (-200 + i * 100))
if user_bet:
    race_is_on=True
while race_is_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winner=turtle.pencolor()
            race_is_on=False
            break
        rand_distance=r.randint(0,10)
        turtle.fd(rand_distance)

if user_bet==winner:
    print(f"You won the bet!!!!!!\nThe winner is {winner}")
else:
    print(f"You lost the bet!!!!!!\nThe winner is {winner}")

srn.exitonclick()
