ROMAN_NUMERALS = [
    (1, 'I'),
    (4, 'IV'),
    (5, 'V'),
    (9, 'IX'),
    (10, 'X'),
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M')
]

def roman_numeral(number):
    if number < 1 or number > 3999:
        raise ValueError('Number must be between 1 and 3999')

    result = ''
    rev_list = sorted(ROMAN_NUMERALS, reverse=True)
    for value, numeral in rev_list:
        while number >= value:
            result += numeral
            number -= value
    return result

if __name__ == '__main__':
    number = int(input())
    print(roman_numeral(number))

