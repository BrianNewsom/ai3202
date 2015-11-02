samples = [0.82, 0.56, 0.08, 0.81, 0.34, 0.22, 0.37, 0.99, 0.55, 0.61, 0.31, 0.66, 0.28, 1.0, 0.95,
0.71, 0.14, 0.1, 1.0, 0.71, 0.1, 0.6, 0.64, 0.73, 0.39, 0.03, 0.99, 1.0, 0.97, 0.54, 0.8, 0.97,
0.07, 0.69, 0.43, 0.29, 0.61, 0.03, 0.13, 0.14, 0.13, 0.4, 0.94, 0.19, 0.6, 0.68, 0.36, 0.67,
0.12, 0.38, 0.42, 0.81, 0.0, 0.2, 0.85, 0.01, 0.55, 0.3, 0.3, 0.11, 0.83, 0.96, 0.41, 0.65,
0.29, 0.4, 0.54, 0.23, 0.74, 0.65, 0.38, 0.41, 0.82, 0.08, 0.39, 0.97, 0.95, 0.01, 0.62, 0.32,
0.56, 0.68, 0.32, 0.27, 0.77, 0.74, 0.79, 0.11, 0.29, 0.69, 0.99, 0.79, 0.21, 0.2, 0.43, 0.81,
0.9, 0.0, 0.91, 0.01]

class Node:
	def __init__(self, name, parents):
		self.name = name
		self.parents = parents
		self.children = []
		self.marginal = 0.0
		self.conditionals = {}
		self.value = None

	def add_child(self, child):
		self.children.append(child)

	def set_value(self, value):
		self.value = value

	def __str__(self):
		return "%s: marginal - %f" % (self.name, self.marginal)

def construct_net():
	cloudy = Node("cloudy", None)
	cloudy.marginal = 0.5

	sprinkler = Node("sprinkler", [cloudy])
	sprinkler.conditionals["c"] = 0.1
	sprinkler.conditionals["~c"] = 0.5

	rain = Node("rain", [cloudy])
	rain.conditionals["c"] = 0.8
	rain.conditionals["~c"] = 0.2

	wet = Node("wet", [sprinkler, rain])
	wet.conditionals["sr"] = 0.99
	wet.conditionals["s~r"] = 0.9
	wet.conditionals["~sr"] = 0.9
	wet.conditionals["~s~r"] = 0

	nodes = [cloudy, sprinkler, rain, wet]
	return nodes

	
if __name__ == "__main__":
 print "hello world"