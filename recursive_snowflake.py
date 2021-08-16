import turtle
koopa = turtle.Turtle()

koopa.penup()
koopa.setpos(-200, 0)
koopa.pendown()
koopa.speed(1000)
def snowflake(side_length, levels):
  for x in range(3):
    snowflake_side(side_length, levels)
    koopa.right(120)

def snowflake_side(side_length, levels):
  #base case is level 0, where it's just equilateral triangle
    if levels == 0:
        koopa.forward(side_length)
    else:
        snowflake_side(side_length/3, levels-1)
        koopa.left(60)
        snowflake_side(side_length/3, levels-1)
        koopa.right(120)
        snowflake_side(side_length/3, levels-1)
        koopa.left(60)
        snowflake_side(side_length/3, levels-1)

snowflake(600, 4)