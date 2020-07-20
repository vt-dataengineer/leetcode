import turtle
import math
v_turtle = turtle.Turtle()
v_turtle.speed(2)
def square():
    v_turtle.forward(100)
    v_turtle.right(90)
    v_turtle.forward(100)
    v_turtle.right(90)
    v_turtle.forward(100)
    v_turtle.right(90)
    v_turtle.forward(100)
# def left():
#     v_turtle.left(90)
#     v_turtle.forward(100)
#     v_turtle.left(90)
#     v_turtle.forward(100)
#     v_turtle.left(90)
#     v_turtle.forward(100)
#     v_turtle.left(45)
#     v_turtle.forward(math.sqrt(20000))

square()
v_turtle.forward(100)
square()
v_turtle.forward(100)
square()
v_turtle.forward(100)
square()
v_turtle.forward(100)



turtle.Screen().exitonclick()
