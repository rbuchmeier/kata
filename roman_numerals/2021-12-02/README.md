# Roman Numeral

## Time

Took about 20 minutes, mostly too a semi-colon error

## Solution

- I took inspiration from this [Java implementation on SO](https://stackoverflow.com/questions/12967896/converting-integers-to-roman-numerals-java) (the concise, recursive one). We don't have a floorkey() function, so I don't have the time complexity of that function, but I do have additional time complexity from having to check every key in the dictionary.
- I could use some sort of binary search to find the floor key, but the possible time complexity gains from such a solution would be at best 5x at a cost of substantial readibility I suspect.
- I did consider using the following return statement: `return roman(num, numerals, [rom for rom in roman_list if rom <= num])`, but I'm pretty sure that adds a fair amount of time complexity and does not really improve the readability anyways. Perhaps if we had a monitoring service to analyze how our users were using this program, we could implement an efficiency improvement if we discovered most of our users were using this to convert small 1-2 digit numbers.
- Overall this solution is quite concise and readable. I could improve the naming a bit.

## Next Steps

Underneath the solution mentioned in the link above, there is another solution that talks about looking at it from a Unary perspective instead of a numbers perspective. It's an intersting idea and would be fun to figure out how to implement on my own.