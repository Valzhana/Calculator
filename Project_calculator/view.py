def view_data(data, title):
    print(f'{title} = {data}')


print('Enter values in order: numerator/denominator for the first fraction; '
      'numerator/denominator for the second fraction. ')


def get_value():
    return int(input('value = '))


def get_value_comp():
    return int(input('value for complex_number = '))
