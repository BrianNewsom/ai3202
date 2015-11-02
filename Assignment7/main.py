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
			elif (wet.conditionals["s~r"] >= scoped_sample[3]):
				wet.set_value(True)
			elif (wet.conditionals["~sr"] >= scoped_sample[3]):
				wet.set_value(True)
			else:
				wet.set_value(False)

def get_total_cloudy(nets):
	cloudy_true = 0
	sprinkler_true = 0
	rain_true = 0
	wet_true = 0
	
	for n in nets:
		if n.nodes["cloudy"].value is True:
			cloudy_true = cloudy_true + 1
		'''
		if n.nodes["sprinkler"].value is True:
			sprinkler_true = sprinkler_true + 1
		if n.nodes["rain"].value is True:
			rain_true = rain_true + 1
		if n.nodes["wet"].value is True:
			wet_true = wet_true + 1
		'''

	return cloudy_true # , sprinkler_true, rain_true, wet_true)

num_trials = 25
def OneA():
	finished_nets = []

	i = iter(samples)
	for _ in range(0, num_trials):
		net = Bayes()
		net.traverse(i)

		finished_nets.append(net)

	cloudy = get_total_cloudy(finished_nets)
	
	probability = float(cloudy) / num_trials
	print "Finished Problem 1A, P(c = true) = {0}".format(probability)

def OneB():
	net = Bayes()
	cloudy = net.nodes["cloudy"]

	print "oops"

if __name__ == "__main__":
	OneA()
	OneB()
