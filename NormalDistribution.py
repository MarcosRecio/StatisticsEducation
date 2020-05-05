from math import e, erf, pi, sqrt

def f(x):
	return (e**((x**2)/-2))/sqrt(2*pi)
def normal_distribution(mean, standard_deviation, x):
	a = 1/standard_deviation
	return a*f((x-mean)/standard_deviation)

def cumulative_distribution(mean, standard_deviation, x):
	m = (x-mean)/(standard_deviation*sqrt(2))
	return (1/2)*(1+erf(m))

def central_limit(mean,standard_deviation, n, weight):
    mean *=n
    standard_deviation *= sqrt(n)
    return cumulative_distribution(mean, standard_deviation, weight)