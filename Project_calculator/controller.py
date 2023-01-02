import model_fractions as model
import model_complex_numbers as comp
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_c = view.get_value()
    value_d = view.get_value()
    model.init(value_a, value_b, value_c, value_d)
    sum = model.get_sum()
    sub = model.get_sub()
    mult = model.get_mult()
    div = model.get_division()
    view.view_data(sum, 'sum')
    view.view_data(sub, 'subtraction result')
    view.view_data(mult, 'multiplication result')
    view.view_data(div, 'division result')


def button_click_comp():
    value_e = view.get_value_comp()
    value_g = view.get_value_comp()
    value_h = view.get_value_comp()
    value_j = view.get_value_comp()
    comp.init(value_e, value_g, value_h, value_j)
    sum = comp.sum_complex()
    sub = comp.sub_complex()
    mult = comp.mult_complex()
    div = comp.div_complex()
    view.view_data(sum, 'sum')
    view.view_data(sub, 'subtraction result')
    view.view_data(mult, 'multiplication result')
    view.view_data(div, 'division result')
