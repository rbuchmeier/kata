# Roman Numerals

## Time

Time was pretty short today. I did 80% of the work in about 15 minutes, the last bit of troubleshooting took me almost another hour (however it was broken up due to being in TN and needing to visit with Ann and her friends).

## Quality

- This was a very concise solution, although a bit dense. It felt much shorter than previous solutions (which seem to err on the 30 lines side vs <20 for this one).
- Breaking the magic numbers into list of integers feels like it made the code more readable. As well as breaking the roman numerals into a list of strings.
- I did not break out any of the more dense logic into their own functions, which would increase testability. If I could come up with good naming conventions for those function I think it would make this a great solution

## Next Steps

- Readibilty of this solution style.
- OOP implementation.
- Measure time for various solution styles (so far, the solution styles seem to be a character map (12/1), if blocked 4s/9s (11/22), no data structures (11/28), and a generic example (11/29)). Some other ideas to try out before timing would be OOP, and creating a list of strings by factor (i.e. [['I', 'II', ... 'IX'], ['X', 'XX', ... 'XC']], etc.)