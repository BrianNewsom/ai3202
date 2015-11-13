import string

class State:
	def __init__(self, letter):
		# Values we need to calculate state data
		self.letter = letter
		self.evidence = []
		self.next = []
		self.count = 0

		# Fields of the HMM
		self.marginal = 0
		self.emissions = {}
		self.transitions = {}

class HMM:
	ALPHABET = string.ascii_lowercase + '_'
	def __init__(self):
		# 'a' -> ['a','b','c','d','e','a']
		# Create states
		self.states = {}
		self.total = 0
		for c in self.ALPHABET:
			s = State(c)
			self.states[c] = s

		self.parse_data();
		self.generate_probabilities()

	def generate_probabilities(self):
		print "<------ Marginals -------->"
		for c in self.ALPHABET:
			s = self.states[c]
			self.gen_marginal(s)
		print "</----- Marginals -------/>"

		print "<------ Emissions -------->"
		for c in self.ALPHABET:
			s = self.states[c]
			self.gen_emissions(s)
		print "</----- Emissions -------/>"
		
		print "<------ Transitions -------->"
		for c in self.ALPHABET:
			s = self.states[c]
			self.gen_transitions(s)
		print "</----- Transitions -------/>"

	def add_evidence(self, s, e):
		self.states[s].evidence.append(e)

	def parse_line(self, l):
		# Return a tuple
		(a, b) = l.split(' ')
		# Kill the new line char
		return (a, b[0])
		
	def gen_emissions(self, s):
		nums = {}
		for c in self.ALPHABET:
			nums[c] = sum(e == c for e in s.evidence)

		for c in self.ALPHABET:
			s.emissions[c] = float(nums[c])/(len(self.states[c].evidence))
			print "P(E[{0}] | X[{1}]) = {2}".format(c, s.letter, s.emissions[c])



	def gen_marginal(self, s):
		try:
			s.marginal = float(s.count) / self.total
			print "P({0}) = {1}".format(s.letter, s.marginal)
		except ZeroDivisionError:
			print "Total is 0"

	def gen_transitions(self, s):
		nums = {}
		for c in self.ALPHABET:
			nums[c] = sum(t == c for t in s.next)

		for c in self.ALPHABET:
			# Smoothen
			s.transitions[c] = float(nums[c] + 1)/(len(self.ALPHABET) + len(s.next))
			print "P(X[{0}] | X[{1}]) = {2}".format(c, s.letter, s.transitions[c])

	def parse_data(self):
		print "Parsing data"
		with open('./data/typos.data') as f:
			prev = ''
			for l in f:
				(s, e) = self.parse_line(l)
				self.states[s].count = self.states[s].count + 1
				self.add_evidence(s, e)
				self.total = self.total + 1

				if prev:
					self.states[prev].next.append(s)

				prev = s

if __name__ == "__main__":
	hmm = HMM()
