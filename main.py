import argparse
import math

class Node:

	def __init__(self, val):
		self.val = val
		# Add these t  simplify
		self.x = 0
		self.y = 0
		self.adjacent = []
		self.parent = None
		# Cost so far 
		self.g = 0
		# Cost of heuristic
		self.h = 0
		# Sum total cost
		self.cost = 0

	def add_edge(self, node):
		self.adjacent.append(node)
	
	def set_loc(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		output = "NODE: val=%s, cost=%s, loc=(%s,%s)" % (self.val, self.cost, self.x, self.y)
		return output 

	
class Graph:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = []
		
		# 2d array of Nodes
		for i in range(0, height):
			self.data.append([])

	def add_to_data(self, node, x):
		# print "adding " + str(node)
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
		if x < 0 or y < 0:
			return None
		else:
			for l in self.data:
				for n in l:
					if n.x is x and n.y is y:
						return n

	def setup_edges(self,x,y):
		node = self.get(x,y)
		# Get nodes
		down_left = self.get(x-1,y-1)
		down = self.get(x,y-1)
		down_right = self.get(x+1,y-1)
		right = self.get(x+1,y)
		up_right = self.get(x+1,y+1)
		up = self.get(x,y+1)
		up_left = self.get(x-1,y+1)
		left = self.get(x-1, y)
		
		for x in [down_left, down, down_right, right, up_right, up, up_left, left]:
			if x is not None and x.val is not 2:
				# Set costs (diag different)
				if x in [down_left, down_right, up_left, up_right]:
					x.g = 14
				else:
					x.g = 10
				
				# We have extra cost if space is a mountain
				if x.val is 1:
					x.g = 10

				node.adjacent.append(x)

		
class AStarSearch:
	
	def __init__(self, start, end):
		self.path = []
		self.start = start
		self.start.cost = 0
		self.end = end

	def heuristic(self, n):
		return 10 * math.sqrt(math.pow((n.x - self.end.x),2) + math.pow((n.y - self.end.y),2))
		
	def update_node(self, node, parent):
		print "Updating parent of " + str(node) + " to " + str(parent)
		node.parent = parent
		# Update actual distance
		node.g = node.g + parent.g
		# Update heuristic
		node.h = self.heuristic(node)
		# Set final cost
		node.cost = node.g + node.h
	
	def search(self):
		print "Beginning search"
		open = [self.start]
		closed = []
		while len(open) > 0:
			print "iter"
			node = min(open, key=lambda n: n.cost)
			open.remove(node)
			if node is not self.end:
				print "Node is not end"
				closed.append(node)
				# Add adjacent edges
				print node.adjacent
				for n in node.adjacent:
					print "Search adjacent node"
					if n not in closed:
						if n in open:
							print "n open"
							# I think this 10 needs to be dynamic
							if n.g > node.g + 10:
								print "replacing cost"
								self.update_node(n, node)
						else:
							print "other replacing cost"
							self.update_node(n, node)
							open.append(n)
			else:
				print "Found end node"
				# Print path
				print "PRINTING PATH"
				cursor = self.end
				# Maximum just in case
				for i in range(0,20):
					if cursor.parent:
						print cursor.parent
						cursor = cursor.parent
		
				
				break
			print "done"
		
		

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

	list_index = 0
	y = height-1
	for line in f:
		if line:
			x = 0
			vals = str.split(line)
			for v in vals:
				n = Node(v)
				n.set_loc(x,y)
				g.add_to_data(n, list_index)
				x = x+1
			y = y-1
			list_index = list_index + 1

	for x in range(0, width):
		for y in range(0, height):
			g.setup_edges(x,y)

	search = AStarSearch(g.get(0,0), g.get(width-1,height-1))
	search.search()

