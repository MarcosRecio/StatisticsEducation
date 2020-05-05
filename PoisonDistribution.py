from math import e, factorial

def poison_distribution(k,l):
	return round(((l**k)*(e**(-l)))/factorial(k), 3)

print(poison_distribution(3,2)) 
