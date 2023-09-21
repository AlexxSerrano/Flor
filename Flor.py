
import turtle
t = turtle.Turtle()
t.pensize(5)

turtle.bgcolor("yellow")  # Cambiamos el color de fondo a amarillo


def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Cambiamos el color de la flor a amarillo
t.pencolor("black")
t.fillcolor("green")

go(0, -250)
t.seth(90)

t.begin_fill()
t.circle(200, 70)
t.circle(-200, 45)
t.seth(270)
t.circle(298, 80)
t.end_fill()

go(0, -250)

t.begin_fill()
t.seth(90)
t.circle(-200, 70)
t.circle(200, 45)
t.seth(270)
t.circle(-298, 80)
t.end_fill()

go(-10, -190)

# Cambiamos el color de las hojas a verde
t.pencolor("black")
t.fillcolor("green")

t.begin_fill()
t.seth(90)
t.goto(-10, 70)
t.seth(0)
t.goto(10, 70)
t.seth(270)
t.goto(10, -190)
t.goto(0, -225)
t.goto(-10, -190)
t.end_fill()

# Continuamos con el color de las hojas a amarillo
t.fillcolor("yellow")

t.pencolor("black")

t.seth(90)
go(-80, 270)
t.begin_fill()
t.circle(-120, 45)
t.seth(320)
t.circle(-120, 45)
t.end_fill()

t.seth(98)
go(-6, 270)
t.begin_fill()
t.circle(-120, 45)
t.seth(320)
t.circle(-120, 45)
t.end_fill()

t.seth(90)
go(-45, 270)
t.begin_fill()
t.circle(-120, 45)
t.seth(320)
t.circle(-120, 45)
t.goto(30, 220)
t.end_fill()

t.seth(0)
go(-10, 70)
t.begin_fill()
t.goto(15, 70)
t.circle(71, 80)
t.seth(80)
t.circle(400, 33)
t.seth(225)
t.circle(300, 25)
t.end_fill

t.seth(0)
go(-10, 70)
t.begin_fill()
t.circle(20, 40)
t.circle(60, 50)
t.seth(90)
t.circle(300, 50)
t.seth(250)
t.circle(400, 33)
t.circle(71, 90)
t.end_fill

t.hideturtle()

turtle.done()
