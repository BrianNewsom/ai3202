import string

class HMM:
	ALPHABET = string.ascii_lowercase + '_'
	def __init__(self):
		# 'a' -> ['a','b','c','d','e','a']
		self.states = {}
		for c in self.ALPHABET:
			self.states[c] = []

	def add_evidence(self, s, e):
		self.states[s].append(e)

	def parse_line(self, l):
		# Return a tuple
		(a, b) = l.split(' ')
		# Kill the new line char
		return (a, b[0])
		
	def gen_probabilities(self, s):
		nums = {}
		probs = {}
		total = len(s)
		for c in self.ALPHABET:
			nums[c] = sum(e == c for e in s)

		for c in self.ALPHABET:
			probs[c] = float(nums[c])/total

		print probs

	def parse_data(self):
		print "Parsing data"
		with open('./data/typos.data') as f:
			for l in f:
				(s, e) = self.parse_line(l)
				self.add_evidence(s, e)

if __name__ == "__main__":
	hmm = HMM()

	hmm.parse_data();
	hmm.gen_probabilities(hmm.states['a'])
