import turtle, math, sympy

unit = 50
painter = turtle.Turtle()
screen = turtle.Screen()

painter.pencolor("blue")
painter.speed(0)
painter.pendown()

WIDTH, HEIGHT = screen.screensize()

points = []

def grid():
    painter.pensize(1)
    painter.pencolor("light grey")
    for x in range(-int(WIDTH/unit), int(WIDTH/unit)):
        painter.penup()
        painter.goto(x*unit, -int(HEIGHT))
        painter.pendown()
        painter.goto(x*unit, int(HEIGHT))
    for y in range(-int(HEIGHT/unit), int(HEIGHT/unit)):
        painter.penup()
        painter.goto(-int(WIDTH), y*unit)
        painter.pendown()
        painter.goto(int(WIDTH), y*unit)
    painter.penup()

def spiral(n):
    painter.pendown()
    painter.pensize(1)
    painter.pencolor("black")
    painter.forward(unit)
    for i in range(16):
        hypo_len = 1/math.sqrt(i+1)
        angle = math.acos(hypo_len)
        angle = 90 - math.degrees(angle)
        painter.left(angle)
        painter.forward(unit)
        x, y = painter.pos()
        painter.goto (0, 0)
        painter.goto (x, y)
        points.append((x/unit, y/unit))

def triangle_length(l):
    sympy.init_printing()
    for n in range(1, 17):
        print("Triangle: ", n)
        print (l)
        sympy.pprint (l * sympy.sqrt(n), use_unicode=True) 
        sympy.pprint (l * sympy.sqrt(n+1), use_unicode=True) 
    print ("-------------------------")

def print_points():
    for i in range(len(points)):
        print ("Point #", str(i), ": ", "%.2f" %points[i][0], "%.2f" %points[i][1])

triangle_length(3)
grid()
painter.goto(0,0)
spiral(16)
print_points()

turtle.done()



