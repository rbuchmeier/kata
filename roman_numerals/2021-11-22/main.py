INT_TO_ROMAN = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def get_nine_or_four(digits):
    string = str(digits)
    if string[0] in ['9', '4']:
        return int(string[0] + '0' * (len(string) - 1))
    return 10000

def get_lower_one(num):
    string = str(num)
    return INT_TO_ROMAN[int('1' + '0' * (len(string) - 1))]

def get_roman_numeral(num):
    if num > 3999:
        return 'Error, number cannot exceed 3999'
    roman = ''
    for key in sorted(INT_TO_ROMAN.keys(), reverse=True):
        while num >= key:
            roman += INT_TO_ROMAN[key]
            num -= key
        if num >= get_nine_or_four(num) and num > key/2:
            roman += get_lower_one(num) + INT_TO_ROMAN[key]
            num -= get_nine_or_four(num)
    return roman 

if __name__ == '__main__':
    print(get_roman_numeral(int(input())))