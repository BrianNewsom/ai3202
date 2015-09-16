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
