import math
from util import *
from Graph import *

class ValueIteration:
	MAX_ITERATIONS = 1000
	ACTIONS = ['right', 'up', 'left', 'down']

	def __init__(self, graph, start=(0,0), gamma=0.9):
		self.path = []
		self.g = graph
		self.states = []
		for l in graph.data:
			for s in l:
				self.states.append(s)
		self.gamma = gamma

	def R(self, state):
		return state.reward

	def T(self, state, action):
		return self.g.setup_edges(state.x, state.y, action, 0.8, 0.1, 0.1)
		
	
	def run(self, epsilon=0.5):
		base_util = {};
		for s in self.states:
			print s
			# Use x,y as index into states
			base_util[(s.x, s.y)] = 0
		for k in range(0, self.MAX_ITERATIONS):
			util = base_util.copy(); 
			delta = 0;
			for s in self.states:
				# Max of all directions
				# Possible actions
				possible_sums = [];
				for a in self.ACTIONS:
					reward_sum = 0
					print self.T(s, a)
					for (p, s1) in self.T(s, a):
						print p
						print s1
						# This ref to U[s1] is sketchy
						reward_sum = reward_sum + p * util[(s1.x, s1.y)]
					possible_sums.append(reward_sum)
				util[(s.x, s.y)] = self.R(s) + self.gamma * max(possible_sums)
				delta = max(delta, abs(util[(s.x, s.y)] - base_util[(s.x, s.y)]))
			if delta < ((epsilon * (1 - self.gamma)) / epsilon):
				return util
				
				
			
