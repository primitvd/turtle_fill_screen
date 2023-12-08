from turtle import Turtle, Screen
import random

screensize = [[0] * 20] * 20
# print(screensize)
screensize[0][0] = 1

t = Turtle()
t.pensize(3)
t.shape("turtle")
global location 
location = [0,0]

screen = Screen()
screen.colormode(255)

def check_angles(loc):
    angles = []
    if t.heading() == 0:
        temp = 0
    elif t.heading() == 90:
        temp = -90
    elif t.heading() == 180:
        temp = -180
    elif t.heading() == 270:
        temp = -270
    if loc[0]+1  < 20 and screensize[loc[0]+1][loc[1]] == 0:
        angles.append(temp)
    if loc[0]-1  >= 0 and screensize[loc[0]-1][loc[1]] == 0:
        angles.append(temp + 180)
    if loc[1]+1  < 20 and screensize[loc[0]][loc[1]+1] == 0:
        angles.append(temp + 90)
    if loc[1]-1  >= 0 and screensize[loc[0]][loc[1]-1] == 0:
        angles.append(temp - 90)
    print(angles)
    return angles

def new_location(loc, direction):
    if direction == 0:
        loc[0] += 1
    elif direction == 180:
        loc[0] -= 1
    elif direction == 90:
        loc[1] += 1
    elif direction == -90:
        loc[1] -= 1
    screensize[loc[0]][loc[1]] = 1
    print(loc)
    return loc

for _ in range(200):
    t.speed(500)
    t.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    angles = check_angles(location)
    # print(angles)
    
    if angles == []:
        break
    direction = random.choice(angles)
    t.left(direction)
    t.forward(20)
    location = new_location(location, direction)



print(t.color())

t.screen.exitonclick()