import argparse

from Node import Node
from Graph import Graph
from ValueIteration import ValueIteration
from util import *
		
			
# Width and height of graph grid, must be redefined for various graphs
WIDTH = 10
HEIGHT = 8
GAMMA = 0.9

if __name__ == "__main__":
	# Command line parser
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", help="The name of the file to treat as the search space")
	parser.add_argument("--epsilon", help="epsilon for value iteration", type=float, default=0.5)
	args = parser.parse_args()

	# open file
	f = open(args.input_file, 'r');
	g = Graph(WIDTH, HEIGHT)

	# Create our graph structure to traverse
	create_graph_from_file(f, g)

	# Create and perform A* search

	v = ValueIteration(g, (0,0), (WIDTH-1,HEIGHT-1), GAMMA, args.epsilon)

	util = v.run()
	v.set_rewards(util)

	path = v.trace_path()
	# Print path to see verbose information about each node on the path 
	#print path
