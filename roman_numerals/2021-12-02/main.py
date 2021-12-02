ROMAN = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]

def roman(num, numerals = '', roman_list=ROMAN):
    if len(roman_list) == 0:
        return numerals
    if num >= roman_list[0][0]:
        factor = (num // roman_list[0][0])
        numerals += roman_list[0][1] * factor
        num -= roman_list[0][0] * factor
    return roman(num, numerals, roman_list[1:])

if __name__ == '__main__':
    print(roman(2500))
