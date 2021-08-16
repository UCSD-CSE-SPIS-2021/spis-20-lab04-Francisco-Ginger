#draw a christmas tree
import turtle

#right turtle
ginger = turtle.Turtle()
ginger.penup()
ginger.speed(5)
#left branches
francisco = turtle.Turtle()
francisco.penup()
francisco.speed(5)
ginger.setpos(0,-200)
ginger.left(90)
def tree(trunk_length, height):
   
    ginger.pendown()
    if height == 0:
        ginger.forward(trunk_length)
        ginger.backward(trunk_length)
    else:
        ginger.forward(trunk_length)
       
        ginger.right(45)
        ginger.backward(trunk_length)
        ginger.left(45)
        return tree(trunk_length * 0.5, height-1)

tree(200, 4)