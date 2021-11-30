ROMAN = 'IVXLCDM'

def get_list_from_number(number):
    return [int(num) for num in str(number)]

def get_roman_from_base(base_indexes, magnitude):
    roman = ""
    for i in base_indexes:
        roman += ROMAN[i + magnitude*2]
    return roman

def convert_number_to_base_indexes(number):
    # Convert a number to a list of indexes, ie, 3 = [0, 0, 0] = [I, I, I]
    # This handles 5-9 by adding 1 to the index
    # and handles the different digits needed by 4 and 9
    base_indexes = ["", "0", "00", "000", "01", "1", "10", "100", "1000", "02"]
    return [int(x) for x in base_indexes[number]]

def roman_numeral(number):
    roman = ''
    number_list = get_list_from_number(number)
    roman = rec_roman(number_list)
    return roman

def rec_roman(list_of_numbers):
    largest_factor = len(list_of_numbers) - 1
    if largest_factor < 0:
        return ''
    largest_num = list_of_numbers[0]
    base_indexes = convert_number_to_base_indexes(largest_num)
    current_roman = get_roman_from_base(base_indexes, largest_factor)
    roman = current_roman + rec_roman(list_of_numbers[1:])
    return roman

if __name__ == '__main__':
    print(roman_numeral(345))
