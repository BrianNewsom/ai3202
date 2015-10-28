class Node:
	def __init__(self, name, abbrev, parents):
		self.name = name
		self.parents = parents
		self.children = []
		self.marginal = 0.0
		self.conditionals = {}
		self.abbrev = abbrev

	def add_child(self, child):
		self.children.append(child)

	def __str__(self):
		return "%s: marginal - %f" % (self.name, self.marginal)

class BayesNet:
	def __init__(self):
		self.nodes = {}

	def create_network(self):
		pollution = Node("pollution", "p", None)
		smoker = Node("smoker", "s", None)

		cancer = Node("cancer", "c", [pollution, smoker])
		pollution.add_child(cancer)
		smoker.add_child(cancer)

		xray = Node("xray", "x", [cancer])
		cancer.add_child(xray)

		dyspnoea = Node("dyspnoea", "d", [cancer])
		dyspnoea.add_child(dyspnoea)

		# Define marginal from info
		pollution.marginal = 0.9
		smoker.marginal = 0.3
		
		# Define conditionals from table
		cancer.conditionals["ps"] = 0.03
		cancer.conditionals["~ps"] = 0.05
		cancer.conditionals["p~s"] = 0.001
		cancer.conditionals["~p~s"] = 0.02

		xray.conditionals["c"] = 0.9
		xray.conditionals["~c"] = 0.2

		dyspnoea.conditionals["c"] = 0.65
		dyspnoea.conditionals["~c"] = 0.3

		for n in [pollution, smoker, cancer, xray, dyspnoea]:
			self.nodes[n.name] = n

		return self.nodes

