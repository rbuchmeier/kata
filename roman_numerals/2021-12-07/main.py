ROMAN = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '', '']
CHARACTER_TEMPLATES = ['', 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'ac']

def int_to_roman(number):
    templates_of_number = [CHARACTER_TEMPLATES[int(i)] for i in str(number)]
    return get_roman(templates_of_number)

def get_roman(numbers, index=0):
    if len(numbers) == 0:
        return ''
    roman_of_digit = numbers[-1].replace('a', ROMAN[index*2]).replace('b', ROMAN[index*2+1]).replace('c', ROMAN[index*2+2])
    return get_roman(numbers[:-1], index+1) + roman_of_digit

if __name__ == '__main__':
    print(int_to_roman(1111))
