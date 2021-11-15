MAPPER = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

def convert_to_roman_numeral(digits):
    roman = ''
    sorted_list = sorted(MAPPER.keys(), reverse=True)
    for i, key in enumerate(sorted_list):
        while digits >= key:
            roman += MAPPER[key]
            digits -= key
    return roman

def get_input(message='0'):
    nums = input(message)
    return int(nums)

def main():
    digits = get_input("Enter number: ")
    print(convert_to_roman_numeral(digits))

if __name__ == '__main__':
    main()
