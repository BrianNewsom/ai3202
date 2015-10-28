# Bayes Network
## Flags
* -g conditional probability
* -j joint probability
* -m marginal probability
* -p to set a prior for Pollution or Smoking

### Example Usages
For example (these are the primary use cases)
* -mD is the marginal probability distribution of Dyspnoea
* -jPSC is the joint probabilities for Pollution, Smoker, and Cancer
* -jpsc is the joint probability for pollution = low, smoker = true, cancer = true
* -j~p~s~c is the joint probability for pollution = high, smoker = false, cancer = false
* -gc|s is the conditional probability for Cancer given that someone is a smoker.
* -pS .40 sets the probability that smoking is True to .40.
* -pP = .80 sets the probability that pollution is Low to .80.

## Appendix

### Probability 

*Marginal probability*: the probability of an event occurring (p(A)), it may be thought of as an unconditional probability.  It is not conditioned on another event.

*Joint probability*:  p(A and B).  The probability of event A and event B occurring.  It is the probability of the intersection of two or more events.

*Conditional probability*:  p(A|B) is the probability of event A occurring, given that event B occurs. 

- See more at: http://sites.nicholas.duke.edu/statsreview/probability/jmc/#sthash.pMVqlzfo.dpuf