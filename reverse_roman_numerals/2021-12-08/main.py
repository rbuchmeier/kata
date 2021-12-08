ROMAN = [
    ('IV', 4),
    ('IX', 9),
    ('XL', 40),
    ('XC', 90),
    ('CD', 400),
    ('CM', 900),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000)
]

def roman_to_int(roman):
    for r in ROMAN:
        roman = roman.replace(r[0], 'I' * r[1])
    return len(roman)

if __name__ == "__main__":
    print(roman_to_int(input("Enter a Roman numeral: ")))
