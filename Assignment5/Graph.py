class Graph:

	def __init__(self, width, height):
		self.data = []

	def add_to_data(self, node, x):
		# Add data to node
		try:
			self.data[x].append(node)
		except IndexError:
			# If out of bounds, add a row
			self.data.append([node])

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
			try:
				# We have our x and y coords switched, simpler access
				return self.data[y][x]
			except IndexError:
				return None
	
	ACTIONS = ['right', 'up', 'left', 'down']

	def setup_edges_node(self, node, main_direction, prob_main, prob_left, prob_right):
		# For any given node, return all adjacent nodes that are valid
		adjacent=[]
		x = node.x
		y = node.y
		# All possible adjacent nodes
		down = self.get(x,y-1)
		if down:
			down.dir = 'down'
		right = self.get(x+1,y)
		if right:
			right.dir = 'right'
		up = self.get(x,y+1)
		if up:
			up.dir = 'up'
		left = self.get(x-1, y)
		if left:
			left.dir = 'left'
		
		for direction in [down, right, up, left]:
			# Don't count as adjacent if it's a wall
			if direction is not None and direction.val is not 2:
				# Set probabilities for given directions
				if direction.dir is main_direction:
					direction.prob = prob_main
				elif direction.dir is self.turn_left(direction.dir):
					direction.prob = prob_left
				elif direction.dir is self.turn_right(direction.dir):
					direction.prob = prob_right
				else:
					# Should I still append these?
					direction.prob = 0

				adjacent.append([direction.prob, direction])
		return adjacent
	
	def turn_left(self, direction): 
		return self.ACTIONS[self.ACTIONS.index(direction)-1]
	
	def turn_right(self, direction):
		return self.ACTIONS[(self.ACTIONS.index(direction)+1) % len(self.ACTIONS)]

	def setup_edges(self,x,y, main_direction, prob_main, prob_left, prob_right):
		# Wraps setup_edges_node if we only have the grid location
		node = self.get(x,y)
		return self.setup_edges_node(node, main_direction, prob_main, prob_left, prob_right)
