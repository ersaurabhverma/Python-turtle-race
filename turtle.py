
from turtle import *
from random import randint
penup()
goto(-140,160)

speed(0)
for step in range(16):
 write(step, align='center')
 right(90)
 forward(10)
 pendown()
 for i in range(10):
   forward(10)
   penup()
   forward(10)
   pendown()
   

 penup()
 backward(210)
 left(90)
 forward(20)


ada=Turtle()
ada.penup()
ada.color('red')
ada.shape('turtle')
ada.goto(-160,140)

lucy=Turtle()
lucy.penup()
lucy.color('yellow')
lucy.shape('turtle')
lucy.goto(-160,120)

july=Turtle()
july.penup()
july.color('green')
july.shape('turtle')
july.goto(-160,100)


bob=Turtle()
bob.penup()
bob.color('blue')
bob.shape('turtle')
bob.goto(-160,80)




for walk in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  july.forward(randint(1,5))
  lucy.forward(randint(1,5))
