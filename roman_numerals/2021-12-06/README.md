# Roman Numerals

Template and Map

## Time

This took me about 25 minutes, although the logic was done in <10.

## Quality

- I really want to like this solution more than the one posted on [12/4](https://github.com/rbuchmeier/kata/blob/master/roman_numerals/2021-12-04/main.py)... but it just isn't quite as readable. It is very hard to justify why this solution would be better for this use case
- However, this does stand out as a potential improvement over [12/1](https://github.com/rbuchmeier/kata/blob/master/roman_numerals/2021-12-01/main.py) in it's language usage of "template" and string usage instead of language of "index" and magic numbers as well as this solution's use of `.replace()`.
- It has become clear that splitting a number into a list of it's digits is very valuable as it removes all need to divide and/or mod.

## Next Steps

I think refactoring the [12/1](https://github.com/rbuchmeier/kata/blob/master/roman_numerals/2021-12-01/main.py) solution or the [12/4](https://github.com/rbuchmeier/kata/blob/master/roman_numerals/2021-12-04/main.py) solution with the experience gained from today's kata would be valuable.
