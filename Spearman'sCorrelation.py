#Spearman's Correlation

def mean(l):
    return sum(l)/len(l)

def standard_deviation(l):
    s = 0
    m = mean(l)
    for i in l:
        s+= (i-m)**2
    return (s/(len(l)))**0.5

def covariance(a,b, n):
    mean_a = mean(a)
    mean_b = mean(b)
    s = 0
    for i in zip(a,b):
        s+= (i[0]-mean_a)*(i[1]-mean_b)
    return s/n

def pearson_correlation(a,b,n):
    return covariance(a,b,n)/(standard_deviation(a)*standard_deviation(b))

def rank(a):
    s = sorted(a)
    return [s.index(i)+1 for i in a]

def spearman_correlation(a,b,n):
    return pearson_correlation(rank(a),rank(b),n)