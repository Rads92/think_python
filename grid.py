def chorse():
    print('stokrotka rosla polna')
    print('a nad nia szumial las')


def repeat_chorse():
    chorse()
    chorse()

# repeat_chorse()


def right_justify(s):
    print(' ' * (70 - len(s)) + s)


def right_justify2(s):
    print(s.rjust(70))


def do_twice(f, v):
    f(v)
    f(v)


def print_spam(title):
    print('spam ' + title)


def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)


def print_line(cols=1):
    print('+' + ('-' * 4 + '+') * cols)


def print_row(cols=1):
    print('|' + (' ' * 4 + '|') * cols)


def add_row(cols, isFirstRow=False):

    if isFirstRow == True:
        print_line(cols)
        do_four(print_row, cols)
        print_line(cols)

        return None

    do_four(print_row, cols)
    print_line(cols)


def print_grid(cols):
    add_row(cols, True)


def print_four_grid():
    add_row(4, True)
    do_four(add_row, 4)


print_grid(2)
# print_four_grid()
