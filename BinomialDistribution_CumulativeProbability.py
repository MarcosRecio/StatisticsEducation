def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def combinations(l,s):
    return factorial(l)/(factorial(s)*factorial(l-s))

def binomialdist(x,n,l):
    combs = combinations(n,x)
    first = l[0]*0.01
    second = 1-first
    return combs*(first**x)*(second**(n-x))

def cumulativeprob_least(x,n,probs):
    s = 0
    for i in range(x,n+1):
        s += binomialdist(i,n,probs)
    return round(s,3)

def cumulativeprob_most(x,n,probs):
    s = 0
    for i in range(x+1):
        s += binomialdist(i,n,probs)
    return round(s,3)

nums = [12,10]

print(cumulativeprob_most(2,10,nums))
print(cumulativeprob_least(2,10,nums))