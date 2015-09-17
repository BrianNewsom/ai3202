import math

class AStarSearch:
	# The maximum number to follow when printing path, in case we have a loop
	MAX_PATH_LENGTH=100
	
	def __init__(self, start, end, g, heuristic):
		self.path = []
		self.start = start
		self.end = end
		self.chosen_heuristic = heuristic
		self.g = g
		# Track locations evaluated for assignment - begin at 1 for start node
		self.locations_evaluated = 1 

	def heuristic(self, n):
		# Dispatches to correct heurstic function
		if self.chosen_heuristic == "manhattan":
			return self.manhattan_distance(n)
		elif self.chosen_heuristic =="diagonal":
			return self.diagonal_distance(n)
		else:
			raise Exception('Invalid choice of heuristic')
	
	def diagonal_distance(self, n):
		dx = abs(n.x - self.end.x)
		dy = abs(n.y - self.end.y)
		return 10 * (dx + dy) + (14 - 2 * 10) * min(dx, dy)
		
	def two_norm_distance(self, n):
		return 14 * math.sqrt(math.pow((n.x - self.end.x),2) + math.pow((n.y - self.end.y),2))

	def manhattan_distance(self, n):
		dx = abs(n.x - self.end.x)
		dy = abs(n.y - self.end.y)
		return 10 * (dx + dy)
		
	def update_node(self, node, parent, move_cost):
		# Update information for a given node - specifically cost and parent
		node.parent = parent
		# Update actual distance
		node.g = move_cost + parent.g
		# Update heuristic
		node.h = self.heuristic(node)
		# Set final cost
		node.cost = node.g + node.h
	
	def search(self):
		# Run actual search algorithm
		# Begin at start node
		open = [self.start]
		closed = []
		while len(open) > 0:
			# Grab minimum cost node out of list
			node = min(open, key=lambda n: n.cost)
			open.remove(node)
			if node is not self.end:
				# If we haven't found the end 
				closed.append(node)
				# Add adjacent edges
				for (adj, move_cost) in self.g.setup_edges_node(node):
					# As long as it is not already finished
					if adj not in closed:
						if adj in open:
								# Check if current path is better than previously found path
							if adj.g > (node.g + move_cost):
								self.update_node(adj, node, move_cost)
						else:
							# Otherwise give it info for the first time and add it to open
							self.update_node(adj, node, move_cost)
							open.append(adj)
							self.locations_evaluated = self.locations_evaluated + 1
			else:
				self.print_output()	
				break
		
	def print_output(self):
		# Print assignment specified output
		path = self.get_path(self.end)
		print """
===========================Search Complete=================================
Successfully finished pathfinding using AStar search with the %s heuristic.
The final cost of the path was %d.
The number of locations traveled was %d.
The optimal path was: 
%s
===========================================================================
		""" % (self.chosen_heuristic, self.end.cost, self.locations_evaluated, path)
		
	def get_path(self, node):
		# Get path to a given node from the start node
		path = []
		cursor = node
		# Maximum just in case
		for i in range(0,self.MAX_PATH_LENGTH):
			if cursor:
				path.append((cursor.x, cursor.y))
				cursor = cursor.parent
		# We want it in reverse order
		return path[::-1]
		
