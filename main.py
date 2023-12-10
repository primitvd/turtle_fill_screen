from turtle import Turtle, Screen
import random



screensize = [[0] * 30] * 30
# print(screensize)
# screensize[0][0] = 1

t = Turtle()
t.pensize(3)
t.shape("turtle")
global location 
location = [0,0]

screen = Screen()
screen.colormode(255)

def check_angles(loc):
    angles = []
    if loc[1]+1  < 19 and screensize[loc[0]][loc[1]+1] == 0:
        print(loc, screensize[loc[0]][loc[1]+1])
        angles.append(0)
    if loc[1]-1  >= 0 and screensize[loc[0]][loc[1]-1] == 0:
        print(loc, screensize[loc[0]][loc[1]-1])
        angles.append(180)
    if loc[0]+1  < 19 and screensize[loc[0]+1][loc[1]] == 0:
        print(loc, screensize[loc[0]-1][loc[1]])
        angles.append(90)
    if loc[0]-1  >= 0 and screensize[loc[0]-1][loc[1]] == 0:
        print(loc, screensize[loc[0]+1][loc[1]])
        angles.append(270)
    print(angles)
    return angles

def new_location(loc, direction):
    if direction == 0:
        loc[1] += 1
    elif direction == 180:
        loc[1] -= 1
    elif direction == 90:
        loc[0] -= 1
    elif direction == 270:
        loc[0] += 1
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
    t.setheading(direction)
    t.forward(20)
    location = new_location(location, direction)



print(t.color())

t.screen.exitonclick()
exit()