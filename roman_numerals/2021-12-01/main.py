ROMAN = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
CHARACTER_INDEXES = [[],[0],[0, 0],[0, 0, 0],[0, 1],[1],[1, 0],[1, 0, 0],[1, 0, 0, 0],[0, 2]]

def roman_numeral(number):
    number_list = [int(i) for i in str(number)]
    roman = build_roman_numeral(number_list)
    return roman

def build_roman_numeral(nums, factor=0):
    if nums == []:
        return ''
    num = nums.pop()
    char_map = CHARACTER_INDEXES[num]
    roman = [ROMAN[i + factor*2] for i in char_map]
    return build_roman_numeral(nums, factor+1) + ''.join(roman)

if __name__ == '__main__':
    print(roman_numeral(int(input())))
