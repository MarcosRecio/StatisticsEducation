#Linear Regression
def mean(l):
    return sum(l)/len(l)
# a, b and coefficient for linear regression
def linear_regression(t):
    n = len(t)
    x = [i[0] for i in t]
    y = [i[1] for i in t]
    s_t = sum([i[0]*i[1] for i in t])
    numerator = (n*s_t)-(sum(x)*sum(y))
    squares_x = sum([i**2 for i in x])
    denominator = (n*squares_x)-sum(x)**2
    b = float(numerator)/float(denominator)
    a = mean(y) - b*mean(x)
    sst = sum([(i-mean(y))**2 for i in y])
    ssr = sum([((a+b*i)-mean(y))**2 for i in x])
    r = (ssr/sst)*100
    return (a,b,r)

# y for a given x value depending on linear regression

def lin_r(t,v):
    a,b,r = linear_regression(t)
    return a+b*v


p = list(range(1,6))
q = [2,1,4,3,5]

linear_regression(zip(p,q))