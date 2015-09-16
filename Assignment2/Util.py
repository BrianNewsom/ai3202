from Node import Node

def create_graph_from_file(f, g, height):
	# Read file, then create nodes in graph g for each entry in the matrix
	list_index = 0
	# We read from top to bottom
	y = height-1
	for line in f:
		if line:
			# Keeps track of x coordinate (read in order)
			x = 0
			# Split on space to get each entry
			vals = str.split(line)
			for v in vals:
				n = Node(v)
				n.set_loc(x,y)
				g.add_to_data(n, list_index)
				x = x+1
			y = y-1
			list_index = list_index + 1
