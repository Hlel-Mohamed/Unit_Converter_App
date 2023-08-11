from constants import *


def convert_length(value, unit_from, unit_to):
    m = value * convertToMeter[unit_from]
    res = m * convertFromMeter[unit_to]
    return res


if __name__ == '__main__':
    result = convert_length(1, 'MILE', 'KM')
    print(f'{result:,.5f}')
