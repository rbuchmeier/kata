# Roman Numeral Conversion

## The Goal

The goal of this project is to convert a number from the decimal system to the roman numeral system.

## The Results

### Time

This project took ~20 minutes to complete, which is the fastest time yet. I probably could have done it in half, except that I wanted a better way to handle 4s/9s without the extra if statements.

### Quality

- Overall, pretty good quality of code.
- Tests are feeling easier to write.
- CoPilot had a probably good suggestion of foregoing the data structure in favor of declaring the rules procedurally. However, once again it did not take into account 4s/9s.
    - The code could have been substantially shorter because of not needing the data structure, but the extra code for 4s/9s ended up not really saving any work over a data structure after all. Because now you need extra if statements for every single 4 and 9.    
    - Having a reliable algorithm for 4s/9s is a needed improvement to all of these katas...one of these days we will have that figured out.

## Next Steps

I still think it is worth trying this with:
- Different data structures
- Real functional programming (recursive?)
- Real object oriented programming (build some class to handle this? Can we use inheritance to solve for 4s/9s?)
