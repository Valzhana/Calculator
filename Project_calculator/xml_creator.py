from user_interface import sum_view
from user_interface import sub_view
from user_interface import mult_view
from user_interface import division_view
from user_interface import sum_comp_view
from user_interface import sub_comp_view
from user_interface import mult_comp_view
from user_interface import division_comp_view


def create():
    xml = '<xml>\n'
    xml += '    <sum/> = >{}</xml>\n' \
        .format(sum_view())
    xml += '    <subtraction/> = >{}</xml>\n' \
        .format(sub_view())
    xml += '    <multiplication/> = >{}</xml>\n' \
        .format(mult_view())
    xml += '    <division/> = >{}</xml>\n' \
        .format(division_view())
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)
    return xml


def create_comp():
    xml = '<xml>\n'
    xml += '    <sum/> = >{}</xml>\n' \
        .format(sum_comp_view())
    xml += '    <subtraction/> = >{}</xml>\n' \
        .format(sub_comp_view())
    xml += '    <multiplication/> = >{}</xml>\n' \
        .format(mult_comp_view())
    xml += '    <division/> = >{}</xml>\n' \
        .format(division_comp_view())
    xml += '</xml>'

    with open('data_new.xml', 'w') as page:
        page.write(xml)
    return xml
