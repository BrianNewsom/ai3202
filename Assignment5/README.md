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

### Very large epsilon

For very large epsilon values (>~25), the value iteration does not give a convergent sequence, e.g.:
```
$ python main.py input/World1MDP.txt --epsilon 30
Found on iteration 9
No path found
```

### Moderate epsilon

For moderate values of epsilon, we get convergence to a solution of the maze.
```
$ python main.py input/World1MDP.txt --epsilon 0.5
Found on iteration 21

===========================Value Iteration Complete========================
Successfully finished pathfinding using Value Iteration.
The epsilon value used was: 0.5
The optimal path was:
[(0,0) util=0.608567069094, (0,1) util=0.845232040408, (0,2) util=1.24401755922, (0,3) util=1.72780216559, (1,3) util=2.46980939975, (1,4) util=3.43029083299, (1,5) util=3.44548810447, (2,5) util=4.7854001451, (3,5) util=6.71647326019, (4,5) util=9.32843508359, (4,6) util=13.0262440081, (4,7) util=18.0920055668, (5,7) util=26.5867585681, (6,7) util=36.9260535668, (7,7) util=52.7451585681, (8,7) util=74.6460535668, (9,7) util=103.745158568]
===========================================================================
```

### Tiny epsilon

For very small values of epsilon, the algorithm converges to the same solution as in the above case.  This suggests the solution is the best the value iteration will get.

```
$ python main.py input/World1MDP.txt --epsilon 0.0000000001
Found on iteration 89

===========================Value Iteration Complete========================
Successfully finished pathfinding using Value Iteration.
The epsilon value used was: 1e-10
The optimal path was:
[(0,0) util=0.684006507633, (0,1) util=0.950009038379, (0,2) util=1.31945699776, (0,3) util=1.83257916356, (1,3) util=2.54524883829, (1,4) util=3.53506783096, (1,5) util=3.52092754301, (2,5) util=4.89017714307, (3,5) util=6.79191269873, (4,5) util=9.43321208156, (4,6) util=13.1016834466, (4,7) util=18.1967825648, (5,7) util=26.6621980066, (6,7) util=37.0308305648, (7,7) util=52.8205980066, (8,7) util=74.7508305648, (9,7) util=103.820598007]
===========================================================================
```
