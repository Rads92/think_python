import turtle


bob = turtle.Turtle()


def draw_koch(t, length):
    if length < 10:
        t.fd(length)
    else:
        section = length / 3
        draw_koch(t, section)
        t.lt(60)
        draw_koch(t, section)
        t.rt(120)
        draw_koch(t, section)
        t.lt(60)
        draw_koch(t, section)


def draw_snowflake(t, length):
    for i in range(3):
        draw_koch(t, length)
        t.rt(120)

draw_snowflake(bob,90)

turtle.mainloop()