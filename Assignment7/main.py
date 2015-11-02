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

class Bayes:
	def __init__(self):
		cloudy = Node("cloudy", None)
		cloudy.marginal = 0.5

		sprinkler = Node("sprinkler", [cloudy])
		sprinkler.conditionals["c"] = 0.1
		sprinkler.conditionals["~c"] = 0.5

		rain = Node("rain", [cloudy])
		rain.conditionals["c"] = 0.8
		rain.conditionals["~c"] = 0.2

		cloudy.add_child(sprinkler)
		cloudy.add_child(rain)

		wet = Node("wet", [sprinkler, rain])
		wet.conditionals["sr"] = 0.99
		wet.conditionals["s~r"] = 0.9
		wet.conditionals["~sr"] = 0.9
		wet.conditionals["~s~r"] = 0

		sprinkler.add_child(wet)
		rain.add_child(wet)

		self.nodes = {}
		self.nodes["cloudy"] = cloudy
		self.nodes["sprinkler"] = sprinkler
		self.nodes["rain"] = rain
		self.nodes["wet"] = wet


	def __str__(self):
		string = "NET\n"
		for n in self.nodes:
			node = self.nodes[n]
			string = string + "{0} - {1}\n".format(n, node.value)

		return string

	def clear_net(self):
		for n in self.nodes:
			n.value = None

	def traverse(self, iterator):
		# Takes in 4 samples
		cloudy = self.nodes["cloudy"]
		sprinkler = self.nodes["sprinkler"]
		rain = self.nodes["rain"]
		wet = self.nodes["wet"]

		scoped_samples = []
		for i in range(0, 4):
			scoped_samples.append(iterator.next())

		if (cloudy.marginal >= scoped_samples[0]):
			cloudy.set_value(True)
			if (sprinkler.conditionals["c"] >= scoped_samples[1]):
				sprinkler.set_value(True)
			else:
				sprinkler.set_value(False)
			
			if (rain.conditionals["c"] >= scoped_samples[2]):
				rain.set_value(True)
			else:
				rain.set_value(False)
		else:
			cloudy.set_value(False)
			if (sprinkler.conditionals["~c"] >= scoped_samples[1]):
				sprinkler.set_value(True)
			else:
				sprinkler.set_value(False)
			
			if (rain.conditionals["~c"] >= scoped_samples[2]):
				rain.set_value(True)
			else:
				rain.set_value(False)

		if (sprinkler.value is True and rain.value is True):
			if (wet.conditionals["sr"] >= scoped_samples[3]):
				wet.set_value(True)
		elif (sprinkler.value is True and rain.value is False):
			if (wet.conditionals["s~r"] >= scoped_samples[3]):
				wet.set_value(True)
		elif (sprinkler.value is False and rain.value is True):
			if (wet.conditionals["~sr"] >= scoped_samples[3]):
				wet.set_value(True)
		else:
			wet.set_value(False)

num_trials = 25
def OneA():
	matching_nets = []

	i = iter(samples)
	for _ in range(0, num_trials):
		net = Bayes()
		net.traverse(i)

		if net.nodes["cloudy"].value:
			matching_nets.append(net)

	probability = float(len(matching_nets)) / num_trials
	print "Finished Problem 1A, P(c = true) = {0}".format(probability)

def OneB():
	matching_nets = []
	i = iter(samples)
	for _ in range(0, num_trials):
		net = Bayes()
		net.traverse(i)
		if net.nodes["rain"].value:
			matching_nets.append(net)

	final_nets = []
	for n in matching_nets:
		if n.nodes["cloudy"].value:
			final_nets.append(n)

	probability = float(len(final_nets)) / len(matching_nets)
	print "Finished Problem 1B, P(c = true | r = true) = {0}".format(probability)

def OneC():
	matching_nets = []
	i = iter(samples)
	for _ in range(0, num_trials):
		net = Bayes()
		net.traverse(i)
		if net.nodes["wet"].value:
			matching_nets.append(net)

	final_nets = []
	for n in matching_nets:
		if n.nodes["sprinkler"].value:
			final_nets.append(n)

	probability = float(len(final_nets)) / len(matching_nets)
	print "Finished Problem 1C, P(s = true | w = true) = {0}".format(probability)

def OneD():
	matching_nets = []
	i = iter(samples)
	for _ in range(0, num_trials):
		net = Bayes()
		net.traverse(i)
		if net.nodes["wet"].value:
			matching_nets.append(net)

	matching_nets2 = []
	for n in matching_nets:
		if n.nodes["cloudy"].value:
			matching_nets2.append(n)
		

	final_nets = []
	for n in matching_nets2:
		if n.nodes["sprinkler"].value:
			final_nets.append(n)

	probability = float(len(final_nets)) / len(matching_nets2)
	print "Finished Problem 1D, P(s = true | c = true, w = true) = {0}".format(probability)


if __name__ == "__main__":
	OneA()
	OneB()
	OneC()
	OneD()
