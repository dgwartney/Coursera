import math
def n_guess(low,high):
	return int(math.ceil(math.log(high - low + 1) /math.log(2)))
