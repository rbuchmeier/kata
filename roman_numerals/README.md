# Roman Numerals

After doing this about a dozen times, it is apparent there are a few different options for converting an integer to roman numerals.

## Techniques

### Parsing the number

Convert the number to a list of digits:
```
[int(d) for d in str(number)]
```

#### Direct mapping
From here, you can map directly to the roman numerals:
```
ROMAN_NUMERALS = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M', 'MM', 'MMM']
]
```
and use the digit list index as the outer roman numeral list index and each number as the indexes for the inner lists. (i.e. a 4 in the hundreds place (3 because 3 digits) is `ROMAN_NUMERALS[3][4]`.

#### Template mapping
Or you can create a template (you could also use 0s, 1s, and 2s, which has more golf potential but less readability imo):
```
['', 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'ac']
```
and a list of roman numberals:
```
ROMAN = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '', '']
```
and then map each digit to the template list (3 => `aaa`, 5 => `b`, 9 => `ac`) and for each of those templates replace the corresponding template with it's roman numeral (either use `enumerate` to get the roman index or use recursion):
```
roman_of_digit = template.replace('a', ROMAN[index*2]).replace('b', ROMAN[index*2+1]).replace('c', ROMAN[index*2+2])
```

### Reduce the number

Create a data structure mapping the numbers and roman equivalent together:
```
roman_numeral_map = (('M', 1000), ('CM', 900), ('D', 500), [ ... ], ('V', 5), ('IV', 4), ('I', 1))
```

Then go down the above data structure, and reduce the number as you append the Roman Numerals to the result:
```
for numeral, integer in roman_numeral_map:
    while number >= integer:
        result += numeral
        number -= integer
```

## Odd solutions

### Unary character replacement

Rather than view this as a numbers problem, this solution views this as a string replacement problem.

First, we replace the number with an associated count of `I`.
```
roman = 'I' * number
```

Then we just go down the line (use a  list of tuples, or just type it out with some regex) and replace an appropriate number of `I`s with higher value characters, then the slightly higher value characters (`V`, `X`, etc..) with higher value characters (`C`, `M`, etc...).
```
result = roman.replace('IIIII', 'V')
result = roman.replace('IIII', 'IV')
result = roman.replace('VV', 'X')
result = roman.replace('VIV', 'IX')
result = roman.replace('XXXXX', 'L')
```
The correct order goes 5, 4, 10, 9, then 50, 40, etc... (Looking carefully at the code for 11-20 should make it apparent).

This makes for a very light solution. As long as it is tested, this is a great solution because it is highely likely for the only change to be input. So some obscurity in the actual order of replacement is unlikely to ruin anyone's day.
