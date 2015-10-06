import math
from util import *
from Graph import *

class ValueIteration:

	def __init__(self, gamma):
		self.gamma = gamma
		self.width = 10
		self.height = 8

	def run(self, graph, eps):
		max_delta = 100
		while max_delta > eps:
			max_delta = 0
			for x in range(0, self.width):
				for y in range(0, self.height):
					node = graph.get(x,y)
					util = node.util
					if node.reward is 50:
						node.util = 50
						node.delta = 0
					else:
						# Find max direction choice
						# Store each sum
						d1 = 0
						d2 = 0
						d3 = 0
						d4 = 0
						up= graph.get(x,y+1)
						down= graph.get(x,y-1)
						right= graph.get(x+1,y)
						left = graph.get(x-1,y)
						if (up and up.val is not 2):
							d1 = d1 + 0.8 * up.util 
							d3 = d3 + 0.1 * up.util
							d4 = d4 + 0.1 * up.util
						else:
							d1 = d1 + 0.8 * node.util
							d3 = d3 + 0.1 * node.util
							d4 = d4 + 0.1 * node.util

						if (down and down.val is not 2):
							d2 = d2 + 0.8 * down.util 
							d3 = d3 + 0.1 * down.util
							d4 = d4 + 0.1 * down.util
						else:
							d2 = d2 + 0.8 * node.util
							d3 = d3 + 0.1 * node.util
							d4 = d4 + 0.1 * node.util

						if (right and right.val is not 2):
							d3 = d3 + 0.8 * right.util 
							d1 = d1 + 0.1 * right.util
							d2 = d2 + 0.1 * right.util
						else:
							d3 = d3 + 0.8 * node.util
							d1 = d1 + 0.1 * node.util
							d2 = d2 + 0.1 * node.util

						if (left and left.val is not 2):
							d4 = d4 + 0.8 * left.util 
							d1 = d1 + 0.1 * left.util
							d2 = d2 + 0.1 * left.util
						else:
							d4 = d4 + 0.8 * node.util
							d1 = d1 + 0.1 * node.util
							d2 = d2 + 0.1 * node.util

						node.util = node.reward + self.gamma * max(d1,d2,d3,d4)
						new_util = node.util
						print new_util

						if (abs(new_util - util) < node.delta):
							node.delta = abs(new_util - util)
						# Set new max delta if we've changed it
						if node.delta > max_delta:
							max_delta = node.delta

	def search(self, graph, x, y):
		node = graph.get(x,y)
		path = [node]
		MAX_ITER = 50
		iter = 0
		while (graph.get(x,y).reward is not 50):
			if iter > MAX_ITER:
				print "Too many iterations, aborting"
				break
			node = graph.get(x,y)
			up= graph.get(x,y+1)
			down= graph.get(x,y-1)
			right= graph.get(x+1,y)
			left = graph.get(x-1,y)
			options = []
			for dir in [up,down,right,left]:
				if (dir and dir.val is not 2):
					options.append(dir.util)
				else:
					options.append(-100000)

			# Now get the max
			max_option = max(options)
			max_option_index = options.index(max_option)
			print options

			# Select from path based on which was chosen as max

			if max_option_index is 0:
				print "going up"
				path.append(up)
				up.parent = node
				y = y+1
			elif max_option_index is 1:
				print "going down"
				path.append(down)
				up.parent = node
				y = y-1
			elif max_option_index is 2:
				print "going right"
				path.append(right)
				right.parent = node
				x = x+1
			else:
				print "going left"
				path.append(left)
				left.parent = node
				x = x-1
			
			iter = iter + 1
		return path

