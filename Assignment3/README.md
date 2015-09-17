# A\* Search
This program computes the A\* Search to provide an optimal route through a given world.

The input files are in the input folders.

The code can be run with
```
	$ python main.py input/World1.txt manhattan
```

As can be discovered using the help flag (-h), there are two options for the heuristic.

## Heuristics
### Manhattan
The manhattan distance is the taxicab distance or one norm, the number of spaces between the start and destination without diagonals.

### Diagonal
Given a choice, I used the diagonal heuristic, computed with (taken from http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html)
```
    dx = abs(node.x - goal.x)
    dy = abs(node.y - goal.y)
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
```
where D is the adjacent distance (10) and D2 is the diagonal distance (14)

I thought it might be optimal because we have a diagonal option.  The one norm ignores this diagonal, but the diagonal heuristic
should prefer it if it makes sense in the world.

## Performance of the two heuristics varied 

### Manhattan

#### World1

```
===========================Search Complete=================================
Successfully finished pathfinding using AStar search with the manhattan heuristic.
The final cost of the path was 156.
The number of locations traveled was 33.
The optimal path was: 
[(0, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (4, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)]
===========================================================================
```

#### World2

```
===========================Search Complete=================================
Successfully finished pathfinding using AStar search with the manhattan heuristic.
The final cost of the path was 142.
The number of locations traveled was 37.
The optimal path was: 
[(0, 0), (1, 0), (2, 0), (3, 1), (3, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)]
===========================================================================
```

### Diagonal

#### World1
```
===========================Search Complete=================================
Successfully finished pathfinding using AStar search with the diagonal heuristic.
The final cost of the path was 130.
The number of locations traveled was 41.
The optimal path was: 
[(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (4, 3), (5, 4), (6, 4), (7, 5), (8, 5), (9, 6), (9, 7)]
=========================================================================== 
```

#### World2
```
===========================Search Complete=================================
Successfully finished pathfinding using AStar search with the diagonal heuristic.
The final cost of the path was 142.
The number of locations traveled was 47.
The optimal path was: 
[(0, 0), (1, 0), (2, 0), (3, 1), (3, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7)]
===========================================================================
```
As is evident in the world1 results, the two algorithms return varying final costs, suggesting one is not optimal.  The Manhattan gives a larger final cost, suggesting it is not optimal, though it visits fewer locations, meaning it is the faster of the two.

However, for world1 with only a few more iterations (visited locations), the diagonal heuristic returns a significantly faster route, and thus is the better choice of the two.

In world2, the heuristics return the same path length, but diagonal visits more locations and thus takes longer to run.  This suggests manhattan is optimal in this case.

All things considered, if speed is desired, Manhattan is the heuristic to use, but for a few more iterations, or if performance is desired, the diagonal heurstic can provide more optimal results if they exist.
