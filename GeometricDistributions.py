def geometric_distribution(n,p):
    q = 1-p
    return (q**(n-1))*p
def cumulative_geometric_distribution(n,p):
    s = 0
    for i in range(1,n+1):
        s+=geometric_distribution(i,p)
    return s
