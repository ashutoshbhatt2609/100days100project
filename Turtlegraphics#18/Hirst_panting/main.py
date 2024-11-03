import turtle as tu
import random
import colorgram
rgb_color=[(235, 211, 228), (217, 223, 218), (104, 125, 106), (213, 91, 152), (140, 150, 140), (186, 32, 62), (225, 109, 212), (199, 173, 147), (237, 225, 215), (105, 170, 112), (177, 47, 159), (218, 219, 224), (186, 9, 19), (38, 21, 40), (27, 63, 25), (26, 22, 42), (223, 194, 167), (42, 101, 44), (205, 58, 87), (58, 54, 68), (132, 132, 136), (190, 218, 187), (230, 172, 176), (231, 82, 65), (235, 211, 228), (217, 223, 218), (104, 125, 106), (213, 91, 152), (140, 150, 140), (186, 32, 62), (225, 109, 212), (199, 173, 147), (237, 225, 215), (105, 170, 112), (177, 47, 159), (218, 219, 224), (186, 9, 19), (38, 21, 40), (27, 63, 25), (26, 22, 42), (223, 194, 167), (42, 101, 44), (205, 58, 87), (58, 54, 68), (132, 132, 136), (190, 218, 187), (230, 172, 176), (231, 82, 65)]
colors=colorgram.extract('image.jpg',100)
for i in colors:
    r=i.rgb.r
    b=i.rgb.b
    g=i.rgb.g
    new_color=(r,b,g)
    rgb_color.append(new_color)
t=tu.Turtle()
t.pu()  #we don't need to be down to draw dots
t.hideturtle() #it looks better when turtle is hidden
t.speed("fastest")
tu.colormode(255)
for j in range(15):
    t.setposition(-750,(-400+50*j))
    for i in range (30):
        t.dot(20,random.choice(rgb_color))
        t.fd(50)

srn=tu.Screen()
srn.exitonclick()

