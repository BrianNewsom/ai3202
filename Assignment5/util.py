from Node import Node

def create_graph_from_file(f, g):
	# Read file, then create nodes in graph g for each entry in the matrix
	# We read from top to bottom
	list_index = 0
	for line in reversed(f.readlines()):
		# Gives false if line is empty - gets rid of empty line
		if line.strip():
			# Split on space to get each entry
			vals = str.split(line)
			for v in vals:
				n = Node(v)
				g.add_to_data(n, list_index)
			list_index = list_index + 1
	set_locations(g)
	
def set_locations(g):
	y = 0
	for l in g.data:
		x = 0
		for node in l:
			node.set_loc(x,y)
			x = x + 1
		y = y + 1

