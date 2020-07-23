import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("Blue")
turtle.setup(600,600)
turtle.shape("turtle")

screen = turtle.Screen()
bob = turtle.Turtle()

def triangle(length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x=0
  while x<3:
    bob.forward(int(length))
    bob.right(120)
    x+=1
  bob.end_fill()

def Circle(radius, color):
  bob.fillcolor(color)
  bob.begin_fill()
  bob.circle(int(radius))
  bob.end_fill()

def Star(length, color):
  bob.fillcolor(color)
  bob.begin_fill()
  x=0
  while x<5:
    bob.forward(int(length))
    bob.right(144)
    x+=1
  bob.end_fill()
  


input_shape = input("What shape do you want to draw?: ")
input_length = input("Choose how big: ")
input_color = input("What color do you want?: ")

if input_shape == "Triangle":
  triangle(input_length, input_color)
elif input_shape == "Circle":
  Circle(input_length,input_color)
elif input_shape == "Star":
  Star(input_length, input_color)
