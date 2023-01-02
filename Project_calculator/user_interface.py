import model_fractions as mod
import model_complex_numbers as m
import logger as log


def sum_view():
    data = mod.get_sum()
    log.sum_logger(data)
    return data


def sub_view():
    data = mod.get_sub()
    log.sub_logger(data)
    return data


def mult_view():
    data = mod.get_mult()
    log.mult_logger(data)
    return data


def division_view():
    data = mod.get_division()
    log.mult_logger(data)
    return data


def sum_comp_view():
    data = m.sum_complex()
    log.sum_logger(data)
    return data


def sub_comp_view():
    data = m.sub_complex()
    log.sub_logger(data)
    return data


def mult_comp_view():
    data = m.mult_complex()
    log.mult_logger(data)
    return data


def division_comp_view():
    data = m.div_complex()
    log.division_logger(data)
    return data
