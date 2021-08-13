import turtle

ginger = turtle.Turtle()
ginger.penup()
ginger.speed(5)
def spiral(initial_length, angle, multiplier):
    ginger.pendown()
    # Base case for stopping the turtle when the initial_length is less than 1 or greater than 200
    if initial_length < 1 or initial_length > 200 :
        ginger.forward(0)
    else:
        ginger.forward(initial_length)
        ginger.right(angle)
        return spiral(initial_length * multiplier, angle, multiplier)

spiral(100, 90, 0.9)
spiral(1, -45, 1.1)