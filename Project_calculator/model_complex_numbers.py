x = 0
y = 0
x_1 = 0
y_1 = 0


def init(e, g, h, j):
    global x
    global y
    global x_1
    global y_1
    x = e
    y = g
    x_1 = h
    y_1 = j


def sum_complex():
    return complex(x, y) + complex(x_1, y_1)


def sub_complex():
    return complex(x, y) - complex(x_1, y_1)


def mult_complex():
    return complex(x, y) * complex(x_1, y_1)


def div_complex():
    return complex(x, y) / complex(x_1, y_1)
