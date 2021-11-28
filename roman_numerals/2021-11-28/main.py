
def get_roman_numeral(number):
    if number < 1 or number > 3999:
        return 'Invalid'

    roman_numeral = ""
    roman_numeral += "M" * (number // 1000)
    if number % 1000 >= 900:
        roman_numeral += "CM"
        number -= 900
    roman_numeral += "D" * (number % 1000 // 500)
    if number % 500 >= 400:
        roman_numeral += "CD"
        number -= 400
    roman_numeral += "C" * (number % 500 // 100)
    if number % 100 >= 90:
        roman_numeral += "XC"
        number -= 90
    roman_numeral += "L" * (number % 100 // 50)
    if number % 50 >= 40:
        roman_numeral += "XL"
        number -= 40
    roman_numeral += "X" * (number % 50 // 10)
    if number % 10 >= 9:
        roman_numeral += "IX"
        number -= 9
    roman_numeral += "V" * (number % 10 // 5)
    if number % 5 >= 4:
        roman_numeral += "IV"
        number -= 4
    roman_numeral += "I" * (number % 5 // 1)
    return roman_numeral

if __name__ == '__main__':
    print(get_roman_numeral(int(input("Enter a number: "))))
