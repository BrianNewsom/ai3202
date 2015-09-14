import argparse

class Node:
	val = 0
	cost = 0
	adjacent = []
	parent = None

	def __init__(self, val):
		self.val = val

	def add_edge(self, node):
		self.adjacent.append(node)

	
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
		try:
			if x < 0 or y < 0:
				return None
			else:
				return self.data[-y][x]
		except:
			return None

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
					x.cost = 14
				else:
					x.cost = 10
				
				# We have extra cost if space is a mountain
				if x.val is 1:
					x.cost = x.cost + 10

				node.add_edge(x)

		
class AStarSearch:
	start = None
	end = None
	path = []
	
	def __init__(self, start, end):
		self.start = start
		self.start.cost = 0
		self.end = end

	def heuristic(self):
		return 1
	
	def search(self):
		open = [self.start]
		closed = []
		while open:
			node = min(open, key=lambda n: n.cost or 9999)
			open.remove(node)
			if node is not self.end:
				closed.append(node)
				# Add adjacent edges
				for n in node.adjacent:
					print n
					cost = self.heuristic()
					n.parent = node
					if n in open:
						if cost < n.cost:
							n.cost = cost
						else:
							n.cost = cost
							open.append(n)
			else:
				break
		
		

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
			g.add_to_data(Node(v), x)
		x = x+1

	for x in range(0, width):
		for y in range(0, height):
			g.setup_edges(x,y)

	search = AStarSearch(g.get(0,0), g.get(width-1,height-1))
	search.search()

