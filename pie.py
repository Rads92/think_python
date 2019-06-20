import turtle
import math
bob = turtle.Turtle()


def draw_triangle(t, length, base_length, base_angle):
	t.fd(length)
	t.lt(180-base_angle)
	t.fd(base_length)
	t.lt(180-base_angle)
	t.fd(length)

def pie(t, n, length):
    angle = 360 / n
    base_angle = (180 - angle) / 2
    sin_angle = math.sin(math.radians(angle / 2))
    base_length = 2 * (sin_angle * length)
    
    for i in range(n):
		draw_triangle(t, length, base_length, base_angle)
        t.rt(180)





turtle.mainloop()
