ROMAN_NUMERALS = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M', 'MM', 'MMM']
]

def int_to_roman(integer):
    roman = ''
    digits = [int(d) for d in str(integer)][::-1]
    for i, d in enumerate(digits):
        roman = ROMAN_NUMERALS[i][d] + roman
    return roman

if __name__ == '__main__':
    print(int_to_roman(int(input())))
