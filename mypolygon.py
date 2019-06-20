import turtle
import math
bob = turtle.Turtle()


def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(90)


def polygon(t, length, n, angle=None):
	if angle == None:
		angle = 360

	for i in range(n):
		t.fd(length)
		t.lt(angle / n)


def circle(t, r):
	l = 2
	obwod = 2 * math.pi * r
	n = int(round(obwod / l))
	polygon(t, l, n)


def arc(t, r, angle):
	obwod = 2 * math.pi * r
	l = 5
	n = int(round(obwod / l * (angle / 360)))
	polygon(t, l, n, angle)


def draw_petal(t, length, n, angle):
	polygon(t, length, n, angle)
	t.lt(180 - angle)
	polygon(t, length, n, angle)
	t.rt(180)


def draw_flower(t, length, petals_amount, angle):
	n = int(length / petals_amount) + 1

	for i in range(petals_amount):
		draw_petal(t, length, n, angle)


def draw_n_flowers(t, length, n, petals_amount):
	angle = 360 / petals_amount

	for i in range(n):
		draw_flower(t, length, petals_amount, angle)
		t.lt(int(angle / 2))


def spiral(t, n):
	for r in range(n):
		polygon(t, r*10, 10, 180)

spiral(bob, 10)

# draw_flower(bob, 50, 10, 72)
# draw_n_flowers(bob, 20, 1, 7)
turtle.mainloop()
