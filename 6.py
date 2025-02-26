from turtle import *
screensize(10000, 10000)
left(90)
down()
pensize(4)
tracer(10)
k = 15
for i in range(777):
	forward(25 * k)
	left(90)
	forward(34 * k)
	left(90)
up()
forward(12 * k)
left(90)
forward(17 * k)
right(90)
down()
for i in range(1996):
	forward(25 * k)
	left(90)
	forward(17 * k)
	left(90)
up()
for i in range(-100, 300):
	for j in range(-100, 100):
		goto(k * i, k * j)
		dot(4, 'red')
done()
