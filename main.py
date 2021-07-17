from math import pow
import turtle
t = turtle.Turtle()
p1 = int(input('Qual o valor do primeiro termo? '))
q = int(input('Qual o valor da razão? '))
for i in range(0, 5):
    an = p1 * pow(q, i)
    #DESENHO
    for j in range(4):
        t.forward(an)
        t.left(90)
