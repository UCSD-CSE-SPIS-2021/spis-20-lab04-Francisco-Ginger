
import turtle

#right turtle
ginger = turtle.Turtle()
ginger.penup()
ginger.speed(1)
#left branches

ginger.setpos(0,-200)
ginger.left(90)
def tree(trunk_length, height):
   
    ginger.pendown()
    if height == 0:
        ginger.forward(trunk_length)
        ginger.backward(trunk_length)
    else:
        ginger.fill("brown")
        ginger.forward(trunk_length)
        ginger.fill("green")
        ginger.right(45)

        tree(trunk_length/1.5, height - 1)

        ginger.left(90)

        tree(trunk_length/1.5, height - 1)

        ginger.right(45)

        ginger.backward(trunk_length)

tree(100, 4)

#fun ideas:
#while drawing trunk make pen brown
#while drawing branches make it green