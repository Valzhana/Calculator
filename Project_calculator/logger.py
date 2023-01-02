from datetime import datetime as dt


def sum_logger(data):
    time = dt.now().strftime('%H: %M')
    with open('log.csv', 'a') as file:
        file.write('{}; sum of fractions; {}\n'.format(time, data))


def sub_logger(data):
    time = dt.now().strftime('%H: %M')
    with open('log.csv', 'a') as file:
        file.write('{}; subtraction result; {}\n'.format(time, data))


def mult_logger(data):
    time = dt.now().strftime('%H: %M')
    with open('log.csv', 'a') as file:
        file.write('{}; multiplication result; {}\n'.format(time, data))


def division_logger(data):
    time = dt.now().strftime('%H: %M')
    with open('log.csv', 'a') as file:
        file.write('{}; division result; {}\n'.format(time, data))
