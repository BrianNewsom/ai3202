class Node:

	def __init__(self, val):
		self.val = int(val)
		# Add these t  simplify
		self.x = int(0)
		self.y = int(0)
		self.parent = None
		# Cost so far 
		self.g = 0
		# Cost of heuristic
		self.h = 0
		# Sum total cost
		self.cost = 0

	def set_loc(self, x, y):
		# Set x and y coords for a node
		self.x = x
		self.y = y
	
	def __repr__(self):
		# Print function for node
		output = "NODE: val=%s, cost so far=%s estimated cost=%s, loc=(%s,%s)" % (self.val, self.g, self.cost, self.x, self.y)
		# Uncomment to view parents (this looks nasty if we leave it, but is helpful for debugging)
		# output = output + " parent=" + str(self.parent)
		return output 
