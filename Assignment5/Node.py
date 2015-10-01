class Node:
	reward_values = {
		0: 0,
		1: -1,
		2: -10000,
		3: -2,
		4: 1,
		50: 50
	}

	def __init__(self, val):
		self.val = int(val)
		# Add these t  simplify
		self.x = int(0)
		self.y = int(0)
		self.parent = None
		# Sum total cost
		self.reward = self.reward_values[int(val)]

	def set_loc(self, x, y):
		# Set x and y coords for a node
		self.x = x
		self.y = y
	
	def __repr__(self):
		# Print function for node
		output = "NODE: val=%s, reward=%s, loc=(%s,%s)" % (self.val, self.reward, self.x, self.y)
		# Uncomment to view parents (this looks nasty if we leave it, but is helpful for debugging)
		# output = output + " parent=" + str(self.parent)
		return output 
