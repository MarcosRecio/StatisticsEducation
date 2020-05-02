x = list(map(int,"10 40 30 50 20 10 40 30 50 20".split()))

w = list(map(int, "1 2 3 4 5 6 7 8 9 10".split()))

def weighted_mean(population,weights):
    addition = 0
    for i in list(zip(population,weights)):
        addition += i[0]*i[1]
    print(addition, sum(weights), round(addition/sum(weights),1))
    return addition/sum(weights)

weighted_mean(x,w)