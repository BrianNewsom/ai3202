import getopt, sys

from bayes import *

def main():
	net = BayesNet()
	net.create_network()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
			# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	for o, a in opts:
		if o in ("-p"):
			# Split into two values, then set the prior in the bayes net
			(variable, new_value) = a.split('=')
			net = set_prior(net, variable, float(new_value))
		elif o in ("-m"):
			print calc_marginal(net, a)
		elif o in ("-g"):
			(var, given) = a.split('|')
			print calc_conditional(net, var, given) 
		elif o in ("-j"):
			print "flag", o
			print "args", a
		else:
			assert False, "unhandled option"
		
    # ...

def set_prior(net, variable, new_value):
	# Set a marginal probability for smoking or pollution
	print "Setting prior for variable {0} to {1}".format(variable, new_value)
	if variable is "P":
		net.nodes["pollution"].marginal = new_value
	elif variable is "S":
		net.nodes["smoker"].marginal = new_value

	# Either way return the new net
	return net

def calc_marginal(net, arg):
	# Takes in bayes net and the arg given (which var we want the marginal for)
	print "Calculating marginal probability for variable {0}".format(arg)

	if arg is "P" or arg is "p":
		return net.nodes["pollution"]

	elif arg is "S" or arg is "s":
		return net.nodes["smoker"]

	elif arg is "C" or arg is "c":
		# We have to actually calculate this time
		pollution = net.nodes["pollution"]
		smoker = net.nodes["smoker"]

		cancer = net.nodes["cancer"]
		# Sum over all possibilities of p and s
		cancer.marginal = cancer.conditionals["ps"]*pollution.marginal + cancer.conditionals["~ps"]*(1-pollution.marginal)*(smoker.marginal) + cancer.conditionals["p~s"]*pollution.marginal*(1-smoker.marginal) + cancer.conditionals["~p~s"]*(1-pollution.marginal)*(1-smoker.marginal)
		return cancer

	elif arg is "D" or arg is "d":
		dyspnoea = net.nodes["dyspnoea"]
		# Calculate cancers marginal if we don't have it
		cancer = net.nodes["cancer"]
		if not cancer.marginal or cancer.marginal is 0:
			net.nodes["cancer"] = calc_marginal(net, "C")
			cancer = net.nodes["cancer"]
		
		dyspnoea.marginal = dyspnoea.conditionals["c"]*cancer.marginal + dyspnoea.conditionals["~c"]*(1-cancer.marginal)
		return dyspnoea

	elif arg is "X" or arg is "x":
		xray = net.nodes["xray"]
		# Calculate cancers marginal if we don't have it
		cancer = net.nodes["cancer"]
		if not cancer.marginal or cancer.marginal is 0:
			net.nodes["cancer"] = calc_marginal(net, "C")
			cancer = net.nodes["cancer"]
		xray.marginal = xray.conditionals["c"]*cancer.marginal + xray.conditionals["~c"]*(1-cancer.marginal)

		return xray

def calc_conditional(net, var, given):
	print "Calculating conditional probability of {0} given {1}".format(var, given)
	if var is given:
		return 1
	else:
		# Now our given probability is 1, so we can calculate a marginal with the first var certain 
		net = set_prior(net, given, 1)
		return calc_marginal(net, var)

	return None

if __name__ == "__main__":
    main()
