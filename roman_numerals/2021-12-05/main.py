ORDER_OF_REPLACEMENT = [
    ('IIIII', 'V'),
    ('IIII', 'IV'),
    ('VV', 'X'),
    ('VIV', 'IX'),
    ('XXXXX', 'L'),
    ('XXXX', 'XL'),
    ('LL', 'C'),
    ('LXL', 'XC'),
    ('CCCCC', 'D'),
    ('CCCC', 'CD'),
    ('DD', 'M'),
    ('DCD', 'CM'),
]

def int_to_roman(number):
    roman = 'I' * number
    for old, new in ORDER_OF_REPLACEMENT:
        roman = roman.replace(old, new)
    return roman

if __name__ == '__main__':
    print(int_to_roman(int(input())))
