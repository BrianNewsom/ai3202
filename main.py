import argparse
import math

class Node:

	def __init__(self, val):
		self.val = int(val)
		# Add these t  simplify
		self.x = int(0)
		self.y = int(0)
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
		output = "NODE: val=%s, cost so far=%s estimated cost=%s, loc=(%s,%s)" % (self.val, self.g, self.cost, self.x, self.y)
		# output = output + " parent=" + str(self.parent)
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

	def setup_edges_node(self, node):
		adjacent=[]
		x = node.x
		y = node.y
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
				additional_cost = 0
				if x in [down_left, down_right, up_left, up_right]:
					additional_cost = 14
				else:
					additional_cost = 10
				
				# We have extra cost if space is a mountain
				if x.val is 1:
					additional_cost = additional_cost + 10

				adjacent.append([x,additional_cost])
		return adjacent

	def setup_edges(self,x,y):
		node = self.get(x,y)
		return setup_edges_node(node)
		
class AStarSearch:
	
	def __init__(self, start, end, g, heuristic):
		self.path = []
		self.start = start
		self.end = end
		self.chosen_heuristic = heuristic
		self.g = g

	def heuristic(self, n):
		if self.chosen_heuristic == "manhattan":
			return self.manhattan_distance(n)
		elif self.chosen_heuristic =="two_norm":
			return self.two_norm_distance(n)
		else:
			raise Exception('Invalid choice of heuristic')
	
	def two_norm_distance(self, n):
		return 10 * math.sqrt(math.pow((n.x - self.end.x),2) + math.pow((n.y - self.end.y),2))

	def manhattan_distance(self, n):
		return 10 * (abs(n.x-self.end.x) + abs(n.y - self.end.y))
		
	def update_node(self, node, parent, move_cost):
		# print "Updating parent of " + str(node) + " to " + str(parent)
		node.parent = parent
		# Update actual distance
		node.g = move_cost + parent.g
		# Update heuristic
		node.h = self.heuristic(node)
		# Set final cost
		node.cost = node.g + node.h
	
	def search(self):
		print "Beginning search"
		open = [self.start]
		closed = []
		while len(open) > 0:
			# print "iter"
			node = min(open, key=lambda n: n.cost)
			open.remove(node)
			if node is not self.end:
				# print "Node is not end"
				closed.append(node)
				# Add adjacent edges
				for (adj, move_cost) in g.setup_edges_node(node):
					# print "Search adjacent node"
					if adj not in closed:
						if adj in open:
							# print "n open"
							# Check if current path is better than previously found path
							if adj.g > (node.g + move_cost):
								self.update_node(adj, node, move_cost)
						else:
							self.update_node(adj, node, move_cost)
							open.append(adj)
			else:
				print "Found end node"
				# Print path
				print "PRINTING PATH"
				cursor = self.end
				print cursor
				# Maximum just in case
				for i in range(0,20):
					if cursor.parent:
						print cursor.parent
						cursor = cursor.parent
		
				
				break
		
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", help="The name of the file to treat as the search space")
	parser.add_argument("heuristic", help="Name of search heuristic to use in A* search", 
		choices=("manhattan", "two_norm"), default="manhattan")
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

	
	#for x in range(0, width):
	#	for y in range(0, height):
	#		g.setup_edges(x,y)

	search = AStarSearch(g.get(0,0), g.get(width-1,height-1), g, args.heuristic)
	search.search()

