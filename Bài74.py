import random
def fnc_random(a,b):
	c = random.random()*b
	if c < a:
		return fnc_random(a,b)
	print(c)

fnc_random(5,95)