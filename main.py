import turtle as t

import random
t.colormode(255)

color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52), (179, 199, 184), (133, 41, 39), (76, 63, 49), (38, 79, 82)]
tortle = t.Turtle()
tortle.shape("arrow")
tortle.color("black")
tortle.penup()
tortle.hideturtle()
tortle.speed("fastest")

def dot():
    for z in range(10):
        color_x = color_list[random.randint(0, 31)]
        tortle.dot(20, color_x)
        tortle.forward(50)

post_y = -220

for g in range(10):
    tortle.setpos(-220, post_y)
    dot()
    post_y += 50









screen = t.Screen()
screen.setup(width=1000, height=1000, startx=0, starty=0)
screen.exitonclick()