from turtle import *
from math import *
import time

G = 0.000098
mass_mars = 1000
mass_venera = 500
r = 100
t = 30
n = 50000

x0, y0 = 0, 0
xv, yv = r, 0
vxv, vyv = 0, sqrt(G * mass_mars / r)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1920, height=1080)
speed(0)
tracer(0)

mars = Turtle()
mars.shape("circle")
mars.color("red")
mars.penup()
mars.goto(x0, y0)
mars.shapesize(3)

venera = Turtle()
venera.shape("circle")
venera.color("blue")
venera.penup()
venera.goto(xv, yv)
venera.shapesize(2)

sim_text = Turtle()
sim_text.hideturtle()
sim_text.color("white")
sim_text.penup()
sim_text.goto(-600, 500)
sim_text.write("Simulation", align="center", font=("Arial", 24, "normal"))

ven_text = Turtle()
ven_text.hideturtle()
ven_text.color("white")
ven_text.penup()
ven_text.goto(-600, 400)
ven_text.write(f"Vener mass: {mass_venera}", align="center", font=("Arial", 24, "normal"))

mars_text = Turtle()
mars_text.hideturtle()
mars_text.color("white")
mars_text.penup()
mars_text.goto(-600, 300)
mars_text.write(f"Mars mass: {mass_mars}", align="center", font=("Arial", 24, "normal"))

for c in range(n):
    R = sqrt((xv - x0) ** 2 + (yv - y0) ** 2)
    F = (G * mass_mars * mass_venera) / (R ** 2)

    axv = -F * (xv - x0) / R / mass_venera
    ayv = -F * (yv - y0) / R / mass_venera

    vxv += axv * t
    vyv += ayv * t

    xv += vxv * t
    yv += vyv * t

    mars.goto(x0, y0)
    venera.goto(xv, yv)

    update()
    time.sleep(0.01)

done()