import string

class State:
	def __init__(self, letter):
		self.letter = letter
		self.conditionals = {}
		self.evidence = []
		self.marginal = 0
		self.count = 0

class HMM:
	ALPHABET = string.ascii_lowercase + '_'
	def __init__(self):
		# 'a' -> ['a','b','c','d','e','a']
		self.states = {}
		self.total = 0
		for c in self.ALPHABET:
			s = State(c)
			self.states[c] = s

	def add_evidence(self, s, e):
		self.states[s].evidence.append(e)

	def parse_line(self, l):
		# Return a tuple
		(a, b) = l.split(' ')
		# Kill the new line char
		return (a, b[0])
		
	def gen_emission(self, s):
		nums = {}
		for c in self.ALPHABET:
			nums[c] = sum(e == c for e in s.evidence)

		emissions = {}
		for c in self.ALPHABET:
			emissions[c] = float(nums[c])/(len(self.states[c].evidence))

		print emissions

	def gen_marginals(self):
		for c in self.ALPHABET:
			s = self.states[c]
			s.marginal = float(s.count) / self.total

	def parse_data(self):
		print "Parsing data"
		with open('./data/typos.data') as f:
			for l in f:
				(s, e) = self.parse_line(l)
				self.states[s].count = self.states[s].count + 1
				self.add_evidence(s, e)
				self.total = self.total + 1

if __name__ == "__main__":
	hmm = HMM()

	hmm.parse_data();
	hmm.gen_emission(hmm.states['_'])
	hmm.gen_marginals()
