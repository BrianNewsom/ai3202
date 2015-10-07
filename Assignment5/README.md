# Value Iteration
## Author: Brian Newsom

This program computes a value iteration to provide an optimal route through a given world. Further parameters can be found in Assignment5.pdf.

The input files are in the input folders.

The code can be run with:
```
	$ python main.py input/World1MDP.txt --epsilon 0.5
```

As can be discovered using the help flag (-h), the epsilon flag is optional and defaults to 0.5.

## Changes in epsilon

Because epsilon can be passed as a command line argument, it is easy to tell whether the output changes for various epsilon values.
