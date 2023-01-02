from user_interface import sum_view
from user_interface import sub_view
from user_interface import mult_view
from user_interface import division_view
from user_interface import sum_comp_view
from user_interface import sub_comp_view
from user_interface import mult_comp_view
from user_interface import division_comp_view


def create():
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>sum of fractions: {} </p>\n' \
        .format(style, sum_view())
    html += '   <p {}>subtraction result: {} </p>\n' \
        .format(style, sub_view())
    html += '   <p {}>multiplication result: {} </p>\n' \
        .format(style, mult_view())
    html += '   <p {}>division result: {} </p>\n' \
        .format(style, division_view())
    html += '   </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)
    return html


def create_comp():
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>addition result: {} </p>\n' \
        .format(style, sum_comp_view())
    html += '   <p {}>subtraction result: {} </p>\n' \
        .format(style, sub_comp_view())
    html += '   <p {}>multiplication result: {} </p>\n' \
        .format(style, mult_comp_view())
    html += '   <p {}>division result: {} </p>\n' \
        .format(style, division_comp_view())
    html += '   </body>\n</html>'

    with open('index_new.html', 'w') as page:
        page.write(html)
    return html
