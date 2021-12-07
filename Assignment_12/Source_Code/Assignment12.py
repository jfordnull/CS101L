########################################################################
##
## CS 101 Lab
## Program #12
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

import turtle

class Point(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class FilledCircle(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

p = Point(-100,100, 'blue')
p.draw()
b = BoxFilled(0,100,200,200,'red','blue')
b.draw()
c = Circle(200,-100,200,'green')
c.draw()
c2 = FilledCircle(-200,-400,300,'orange','orange')
c2.draw()
p.draw()