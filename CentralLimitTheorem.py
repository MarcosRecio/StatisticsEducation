#Central Limit Theorem
from math import e, erf, pi, sqrt

def f(x):
	return (e**((x**2)/-2))/sqrt(2*pi)
def normal_distribution(mean, standard_deviation, x):
	a = 1/standard_deviation
	return a*f((x-mean)/standard_deviation)

def central_limit(mean,standard_deviation, n):
	mean *= n
	standard_deviation *= sqrt(n)
	return normal_distribution(mean, standard_deviation,perbox)
	

