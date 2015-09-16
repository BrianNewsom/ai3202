class Graph:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.data = []
		# 2d array of Nodes
		for i in range(0, height):
			self.data.append([])

	def add_to_data(self, node, x):
		# Add data to node
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
		# Get node at given location, or if it doesn't exist return None
		if x < 0 or y < 0:
			return None
		else:
			for l in self.data:
				for n in l:
					if n.x is x and n.y is y:
						return n

	def setup_edges_node(self, node):
		# For any given node, return all adjacent nodes that are valid
		adjacent=[]
		x = node.x
		y = node.y
		# All possible adjacent nodes
		down_left = self.get(x-1,y-1)
		down = self.get(x,y-1)
		down_right = self.get(x+1,y-1)
		right = self.get(x+1,y)
		up_right = self.get(x+1,y+1)
		up = self.get(x,y+1)
		up_left = self.get(x-1,y+1)
		left = self.get(x-1, y)
		
		for x in [down_left, down, down_right, right, up_right, up, up_left, left]:
			# Don't count as adjacent if it's a wall
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
		# Wraps setup_edges_node if we only have the grid location
		node = self.get(x,y)
		return setup_edges_node(node)
