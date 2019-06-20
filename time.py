import time
import turtle

bob = turtle.Turtle()


def from_unix_to_today():
    days_in_seconds = 60 * 60 * 24
    unix_time = time.time()
    days_from_unix_time = unix_time // days_in_seconds
    today_seconds = unix_time % days_in_seconds
    hours = today_seconds // (60 * 60)
    minutes = (today_seconds % (60 * 60)) // 60
    seconds = (today_seconds % (60 * 60)) % 60

    print("It is {} days from 01.01.1970 and today is {}:{}:{}"
          .format(
              days_from_unix_time,
              hours,
              minutes,
              seconds
          ))


def check_fermat():
    a = int(input('Podaj a: \n'))
    b = int(input('Podaj b: \n'))
    c = int(input('Podaj c: \n'))
    n = int(input('Podaj n: \n'))

    if n > 2:
        if a**n + b**n == c**n:
            print('Do licha, Fermat sie mylil')
        else:
            print('Nie,to nie dziala')


def is_triangle():
    a = int(input('Podaj a: \n'))
    b = int(input('Podaj b: \n'))
    c = int(input('Podaj c: \n'))

    if a + b > c and b + c > a and a + c > b:
        print('Tak')
    else:
        print('Nie')


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)


def koch(t, length):
    if length < 30:
        t.fd(length)
        return
    
    odc = length/3

    koch(t, odc)
    t.lt(60)
    koch(t, odc)
    t.rt(120)
    koch(t, odc)
    t.lt(60)
    koch(t, odc)


def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        t.rt(120)

snowflake(bob, 90)

turtle.mainloop()
