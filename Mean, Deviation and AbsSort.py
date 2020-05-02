def mean(*args):
    l = []
    s = 0
    for arg in args:
        l.append(float(arg))
        s += arg # s = s + arg
    return s/len(l)

print(mean(5,10,3,2,7,8))

print(mean(5,7,5,20,34,53,4,6,3))

def deviation(*args):
    l = []
    m = float(mean(args[0]))
    for arg in args:
        l.append(float(arg)- m)
    return l

print(deviation(5,10,3,2,7,8))


def absort(*args):
    l = []
    for arg in args:
        l.append(arg)
    return sorted(l, key = lambda x : abs(x))

print(absort(-20,-5,10,15))
