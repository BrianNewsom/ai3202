from Node import Node

def create_graph_from_file(f, g, height):
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
