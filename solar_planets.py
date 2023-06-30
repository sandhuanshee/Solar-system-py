import turtle
import math

#creating screen
screen = turtle.Screen()
screen.tracer(50)

#creating sun
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

#creating planets's data
class Planet(turtle.Turtle):
    def __init__(self, name, radius, color):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*math.cos(self.angle) # Angle in radians
        y = self.radius*math.sin(self.angle)

        self.goto(sun.xcor()+x, sun.ycor()+y)

#making Planets
mercury = Planet("Mercury",40, 'grey')
venus = Planet("Venus", 80, 'orange')
earth = Planet("Earth", 100, 'blue')
mars = Planet("Mars", 150, 'red')
jupiter = Planet("Jupiter",180,'brown')
saturn = Planet("Saturn", 230, 'pink')
uranus = Planet("Uranus", 250, 'light blue')
neptune = Planet("Neputune", 280, 'black')

#adding planets in a list
Planets = [mercury,venus, earth, mars, jupiter, saturn, uranus, neptune]
 
def radian(mercury, venus, earth, mars, jupiter, saturn, uranus, neptune):
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005

while True:
   screen.update()
   for i in Planets:
       i.move()#moving the elements of the list
       radian(mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)

 
 
