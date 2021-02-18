##From a Crash Course: Intro to Python hosted via Meetup by Momentum Learning
## December 2020
## Repl.it may be used to run the program

#Load the Turtle utility for drawing
import turtle

#Set the color of the arrow and lines to red
turtle.color("#ef233c")

#Counter will be the beginning location of the drawing
counter =  0

#The object is to draw a box.
#Each time it gets to the end of the line and turns the counter is upped by 1
#At 4 there will be 4 sides to the box
#For the box size it will be 100 pixels on each side
#Right 90 will turn it right for the corner of the square
while counter < 4:
  turtle.forward(100)
  turtle.right(90)
  counter += 1

#Box is done, arrow stops moving.
turtle.done()
