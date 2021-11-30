def roman_numeral(number):
    if number < 1 or number > 3999:
        return "Invalid"
    roman_numeral_map = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    result = ''
    for numeral, integer in roman_numeral_map:
        while number >= integer:
            result += numeral
            number -= integer
    return result

if __name__ == '__main__':
    print(roman_numeral(int(input("Enter a number: "))))
