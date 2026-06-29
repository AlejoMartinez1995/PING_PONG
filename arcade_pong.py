'''Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los
controles del usuario para las paletas de los jugadores izquierda y derecha.
El juego debe incluir una pelota que se mueva por la pantalla, rebotando en las paredes y las paletas de los jugadores. 
El objetivo del juego es que cada jugador intente evitar que la pelota pase más allá de su paleta, anotando puntos cuando la pelota pasa la paleta del oponente.'''

import turtle
import random
import time

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paleta izquierda
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Paleta derecha
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-3, 3])
ball.dy = random.choice([-3, 3])

# Funciones para mover las paletas
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 20)

def left_paddle_down():
    y = left_paddle.ycor()
    if y > -250:
        left_paddle.sety(y - 20)

def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_paddle_down():
    y = right_paddle.ycor()
    if y > -250:
        right_paddle.sety(y - 20)

# Asignar teclas
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "i")
screen.onkeypress(right_paddle_down, "j")

# Bucle principal del juego
while True:
    time.sleep(0.005) 
    screen.update()

    # Mover la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Colisiones con las paredes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Colisiones con las paletas
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Puntos
    if ball.xcor() > 390:
        print("Jugador izquierdo anota un punto!")
        ball.goto(0, 0)
        ball.dx = random.choice([-3, 3])
        ball.dy = random.choice([-3, 3])

    if ball.xcor() < -390:
        print("Jugador derecho anota un punto!")
        ball.goto(0, 0)
        ball.dx = random.choice([-3, 3])
        ball.dy = random.choice([-3, 3])