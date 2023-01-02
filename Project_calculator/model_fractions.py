from fractions import Fraction

numer_1 = 0
numer_2 = 0
den_1 = 0
den_2 = 0


def init(a, b, c, d):
    global numer_1
    global den_1
    global numer_2
    global den_2
    numer_1 = a
    den_1 = b
    numer_2 = c
    den_2 = d


def get_sum():
    return Fraction(numer_1, den_1) + Fraction(numer_2, den_2)


def get_sub():
    return Fraction(numer_1, den_1) - Fraction(numer_2, den_2)


def get_mult():
    return Fraction(numer_1, den_1) * Fraction(numer_2, den_2)


def get_division():
    return Fraction(numer_1, den_1) / Fraction(numer_2, den_2)
