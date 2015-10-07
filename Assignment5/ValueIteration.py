import math
from util import *
from Graph import *

class ValueIteration:
	MAX_ITERATIONS = 100
	ACTIONS = ['right', 'up', 'left', 'down']
	ACTIONS_VECTORS = [(1,0), (0,1), (-1, 0), (0, -1)]

	def __init__(self, graph, start=(0,0), end=(9,7), gamma=0.9):
		self.path = []
		self.g = graph
		self.states = []
		for l in graph.data:
			for s in l:
				self.states.append(s)
		self.gamma = gamma
		self.start = start
		self.end = end

	def R(self, state):
		return state.reward

	def T(self, state, action):
		if state.val is 2:
			# If we can't go there
			return [(0.0, state)]
		else:	
			return self.g.setup_edges(state.x, state.y, action, 0.8, 0.1, 0.1)
		
	
	def run(self, epsilon=0.5):
		new_util= dict([((s.x,s.y), 0) for s in self.states])
		for iter in range(0, self.MAX_ITERATIONS):
			util = new_util.copy()
			delta = 0
			for s in self.states:
				# Max of all directions
				# Possible actions
				possible_sums = []
				for a in self.ACTIONS:
					reward_sum = 0
					for (p, s1) in self.T(s, a):
						# This ref to U[s1] is sketchy
						reward_sum = reward_sum + p * util[(s1.x, s1.y)]
					possible_sums.append(reward_sum)
				maximized = max(possible_sums)
				# Get index so we know which action was chosen. This corresponds to our actions index
				max_index = possible_sums.index(maximized)
			
				action_chosen = self.ACTIONS[max_index]
				s.action = action_chosen
				new_util[(s.x, s.y)] = self.R(s) + self.gamma * max(possible_sums)
				delta = max(delta, abs(util[(s.x, s.y)] - new_util[(s.x, s.y)]))
			if delta < ((epsilon * (1 - self.gamma)) / self.gamma ):
				print "Found on iteration %d" % iter
				return util


	def set_rewards(self, reward_dict):
		for s in self.states:
			s.reward = reward_dict[(s.x,s.y)]
		return

	def trace_path(self):
		max_path_length = 100
		start_node = self.g.get(self.start[0],self.start[1])
		end_node = self.g.get(self.end[0],self.end[1])
		
		path = [start_node]
		# Initialize s to start_node
		s = start_node
		for i in range(0, max_path_length):
			vector_index = self.ACTIONS.index(s.action)
			movement = self.ACTIONS_VECTORS[vector_index]
			new_coord = tuple_add((s.x,s.y),movement)
			s = self.g.get(new_coord[0], new_coord[1])
			path.append(s)
			if s is end_node:
				return path
		print "No path found"
		return None
