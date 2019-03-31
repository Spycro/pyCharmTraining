import turtle
import math


def polygon(t, length, side):
    for i in range(side):
        t.fd(length)
        t.lt(360/side)


def circle(t, r):
    circonference = r*math.pi*2
    n = int(circonference / 3) +3
    length = circonference / n
    polygon(t,length, n)



def arc(t, r, angle):
    for i in range(angle):
        t.fd(1)
        t.lt(1)


bob = turtle.Turtle()
print(bob)

arc(bob, 10, 360)


turtle.mainloop()