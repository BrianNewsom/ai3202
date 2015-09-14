import argparse

class Node:
	val = 0
	adjacent_edges = []

	def __init__(self, val):
		self.val = val

	def add_edge(self, node):
		adjacent_edges.append(node)

	
class Graph:
	width = 0
	height = 0
	data = []

	def __init__(self, width, height):
		self.width = width
		self.height = height
		
		# 2d array of Nodes
		for i in range(0, height):
			self.data.append([])

	def add_to_data(self, node, x):
		self.data[x].append(node)

	def print_graph(self):
		# Print out graph in human readable way to verify
		for i in range(0, self.width):
			print "i: %d" % i
			print ""
			for j in range(0, self.height):
				print "j: %d" % j
				print self.data[j][i].val
	
	def get(self, x, y):
		# Index from bottom left corner (start node)
		# Because of the list composition, we do this in reverse of traditional order
		return self.data[height - 1 - y][x]
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", help="The name of the file to treat as the search space")
	parser.add_argument("heuristic", help="Name of search heuristic to use in A* search")
	args = parser.parse_args()

	width = 10
	height = 8
	# open file
	f = open(args.input_file, 'r');
	g = Graph(width, height)

	x = 0 #height
	for line in f:
		vals = str.split(line)
		for v in vals:
			print v
			g.add_to_data(Node(v), x)
		x = x+1
	
