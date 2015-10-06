import math
from util import *
from Graph import *

class ValueIteration:
	MAX_ITERATIONS = 1
	ACTIONS = ['right', 'up', 'left', 'down']
	ACTIONS_VECTORS = [(1,0), (0,1), (-1, 0), (0, -1)]

	def __init__(self, graph, start=(0,0), end=(9,7), gamma=0.9):
		self.path = []
		self.g = graph
		self.states = []
		for l in graph.data:
			for s in l:
				self.states.append(s)
		self.matrix = graph.data
		self.gamma = gamma
		self.start = start
		self.end = end

	def R(self, state):
		return state.reward

	def T(self, state, action):
		print "Running T"
		print state
		if state.val is 2:
			# If we can't go there
			print "val is 2"
			return [(0.0, state)]
		else:	
			options = self.g.setup_edges(state.x, state.y, action, 0.8, 0.1, 0.1)
			print options
			return options
		
	
	def run(self, epsilon=0.5):
		max_delta = 100
		iterations = 0
		while max_delta > epsilon:
			if iterations > self.MAX_ITERATIONS:
				print "Too many iterations :/"
				print self.g.data
				return
			for x in range(0,10):
				for y in range(8-1, -1, -1):
					node = self.g.get(x,y)
					util = node.util
					if node.reward is 50:
						node.util=50
						node.delta=0
					else:
						# Possible actions
						possible_sums = []
						for a in self.ACTIONS:
							reward_sum = 0
							for (p, s1) in self.T(node, a):
								# This ref to U[s1] is sketchy
								reward_sum = reward_sum + p * s1.util 
							possible_sums.append(reward_sum)
						maximized = max(possible_sums)
						# Get index so we know which action was chosen. This corresponds to our actions index
						max_index = possible_sums.index(maximized)
					
						action_chosen = self.ACTIONS[max_index]
						node.action = action_chosen
						node.util = self.R(node) + self.gamma * max(possible_sums)
						new_util=node.util
					node.delta = max(node.delta, abs(new_util - util))
					if node.delta > max_delta:
						max_delta = node.delta
			iterations = iterations + 1

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
			if s is end_node or not s:
				return path
		print "No path found"
		return None
