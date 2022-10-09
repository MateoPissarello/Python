
import turtle
import os
import time
import random


posponer = 0.1
#Configuracion de la ventana
window = turtle.Screen() #Inicializar una ventana gráfica
window.title("Snake game 🐍") #Titulo de la ventana
window.bgcolor("black") #Cambiar el color del fondo
window.setup(width=600,height=600) #Modificar tamaño inicial de la ventana
window.tracer(0) #hace mejor las animaciones

#Crear la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup() #El turtle no deja rastro
cabeza.goto(0,0) #Posicion en pantalla 
cabeza.direction = "stop"
turtle.register_shape("manzana.gif")
#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("manzana.gif")
comida.resizemode("auto")
#comida.color("red")
comida.penup() #El turtle no deja rastro
comida.goto(0,100) #Posicion en pantalla 

#Segmentos / cuerpo serpiente
segmentos = []
#Funciones
def up():
    cabeza.direction = "up"
def down():
    cabeza.direction = "down"
def left():
    cabeza.direction = "left"
def right():
    cabeza.direction = "right"

def serpienteMoviento():
    if cabeza.direction == "up":
        y = cabeza.ycor() #ycor obtiene la coordenada y de nuestro elemento
        cabeza.sety(y+20) #sety modifica la coordenada y de nuestro elemento
    if cabeza.direction == "down":
        y = cabeza.ycor() 
        cabeza.sety(y-20) 
    if cabeza.direction == "right":
        x = cabeza.xcor() #xcor obtiene la coordenada x de nuestro elemento
        cabeza.setx(x+20) #setx modifica la coordenada x de nuestro elemento
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-20)
#Teclado
window.listen()
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
while True:
    window.update()
    if cabeza.distance(comida) < 40:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
        nuevoSegmento = turtle.Turtle()
        nuevoSegmento.speed(0)
        nuevoSegmento.shape("square")
        nuevoSegmento.color("green")
        nuevoSegmento.penup() #El turtle no deja rastro
        segmentos.append(nuevoSegmento)
    #mover el cuerpo de la serpiente
    totalSegmentos = len(segmentos)
    for i in range(totalSegmentos -1, 0,-1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x,y)
    if totalSegmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)


    serpienteMoviento()
    time.sleep(posponer)