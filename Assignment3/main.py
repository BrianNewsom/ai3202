import argparse

from Node import Node
from Graph import Graph
from AStarSearch import AStarSearch
from Util import *
		
			
# Width and height of graph grid, must be redefined for various graphs
WIDTH = 10
HEIGHT = 8

if __name__ == "__main__":
	# Command line parser
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", help="The name of the file to treat as the search space")
	parser.add_argument("heuristic", help="Name of search heuristic to use in A* search", 
		choices=("manhattan", "diagonal"), default="manhattan")
	args = parser.parse_args()

	# open file
	f = open(args.input_file, 'r');
	g = Graph(WIDTH, HEIGHT)

	# Create our graph structure to traverse
	create_graph_from_file(f, g, HEIGHT)

	# Create and perform A* search
	search = AStarSearch(g.get(0,0), g.get(WIDTH-1,HEIGHT-1), g, args.heuristic)
	search.search()

