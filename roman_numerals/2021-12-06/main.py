TEMPLATE = ['', 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'ac']
ROMAN_NUMERALS = [
    ('I', 'V', 'X'),
    ('X', 'L', 'C'),
    ('C', 'D', 'M'),
    ('M', '', '')
]

def template_to_roman(template, index):
    return template.replace('a', ROMAN_NUMERALS[index][0]).replace('b', ROMAN_NUMERALS[index][1]).replace('c', ROMAN_NUMERALS[index][2])

def get_roman_from_templated_list(templates):
    if len(templates) == 0:
        return ''
    return template_to_roman(templates[0], len(templates) - 1) + get_roman_from_templated_list(templates[1:])

def int_to_roman(number):
    templated_list = [TEMPLATE[int(i)] for i in str(number)]
    return get_roman_from_templated_list(templated_list)

if __name__ == '__main__':
    print(int_to_roman(int(input())))
