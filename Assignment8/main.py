import string
import math

ALPHABET = string.ascii_lowercase + '_'

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

	def gen_emissions(s):
		nums = {}
		for c in ALPHABET:
			nums[c] = sum(e == c for e in s.evidence)

		for c in ALPHABET:
			s.emissions[c] = float(nums[c] + 1)/(len(ALPHABET) + len(s.evidence))
			# print "P(E[{0}] | X[{1}]) = {2}".format(c, s.letter, s.emissions[c])

	def gen_marginal(s, total):
		try:
			s.marginal = float(s.count) / total
			#print "P({0}) = {1}".format(s.letter, s.marginal)
		except ZeroDivisionError:
			print "Total is 0"

	def gen_transitions(s):
		nums = {}
		for c in ALPHABET:
			nums[c] = sum(t == c for t in s.next)

		for c in ALPHABET:
			# Smoothen
			s.transitions[c] = float(nums[c] + 1)/(len(ALPHABET) + len(s.next))
			#print "P(X[{0}] | X[{1}]) = {2}".format(c, s.letter, s.transitions[c])

class HMM:
	def __init__(self):
		# 'a' -> ['a','b','c','d','e','a']
		# Create states
		self.states = {}
		self.total = 0
		for c in ALPHABET:
			s = State(c)
			self.states[c] = s

		self.parse_data();
		self.generate_probabilities()

	def generate_probabilities(self):
		print "<------ Marginals -------->"
		for c in ALPHABET:
			s = self.states[c]
			s.gen_marginal(self.total)
		print "</----- Marginals -------/>"

		print "<------ Emissions -------->"
		for c in ALPHABET:
			s = self.states[c]
			s.gen_emissions()
		print "</----- Emissions -------/>"
		
		print "<------ Transitions -------->"
		for c in ALPHABET:
			s = self.states[c]
			s.gen_transitions()
		print "</----- Transitions -------/>"

	def add_evidence(self, s, e):
		self.states[s].evidence.append(e)

	def parse_line(self, l):
		# Return a tuple
		(a, b) = l.split(' ')
		# Kill the new line char
		return (a, b[0])

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

	def viterbi(self, data):
		# After initialization - run viterbi on some data
		V = [{}]
		path = {}

		def log(x):
			base = 10
			return math.log(x, base)

		# Initialize base case
		for c in self.states:
			s = self.states[c]
			V[0][c] =10 +  s.emissions[data[0]]
			path[c] = [c]
		print "Finished initializing"
			
		def get_max_next(t,c):
			options = []
			for s0 in self.states:
				a = 10 + V[t-1][s0]
				b = s.transitions[s0]
				c = s.emissions[data[t]]
				try:
					if a > 0 and b > 0 and c > 0:
						(prob, state) = (a + log(b) + log(c), s0)
						options.append((prob, state))
					else:
						print a
		
				except ValueError:
					print "Tried to log 0"

			mx = (0, None)
			if options:
				mx = max(options) 
			return mx

		# Run viterbi
		for t in range(1, len(data)):
			V.append({})
			tmp_path = {}
			for c in self.states:
				s = self.states[c]
				(prob, state) = get_max_next(t,c)
				if state:
					V[t][c] = prob
					tmp_path[c] = path[state] + [c]
			
			# Set optimal for each path
			path = tmp_path

		n = len(data) - 1
		(prob, state) = max((V[n][c], c) for c in self.states)
		print data
		print path[state]
		return (prob, path[state])

def get_viterbi_input(file_name):
	data = []
	with open(file_name) as f:
		for l in f:
			data.append(l[2])

	return data

if __name__ == "__main__":
	hmm = HMM()

	data = get_viterbi_input('./data/typos20_test.data')

	hmm.viterbi(data)

