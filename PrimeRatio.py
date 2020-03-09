import pygal

def fibonacci(limit):
    fibs = []
    for i in range(limit):
        if i<=1:
            fibs.append(i)
        else:
            fibs.append(fibs[i-2]+fibs[i-1])
    print(str(len(fibs))+" Fibonacci nums")
    return fibs
    

def prime(num):
    nums = list(range(2, int(num)+1))
    nondiv = []
    prime = [2]
    while len(nums)!=0:
        for i in nums:
            if i%int(prime[-1])!=0:
                nondiv.append(i)
        prime.append(nondiv[0])
        nums = nondiv
        nondiv = []
        if len(nums)==1:
            prime.append(nums[0])
            print(str(len(prime))+" Prime nums")
            return prime

line = pygal.Line()
total = 500
jump = 100
#Creating a title
line.title = "Prime numbers and Fibonacci Numbers percentage per total first natural numbers"

line.x_labels = map(str, range(10,total,jump))

#Adding Data
line.add("Ratio Primes", [len(prime(a))/a for a in range(10,total,jump)])
#line.add("Primes",[4,15,25,95,168,669,1229,5133,9592,78498])
line.add("Ratio Fibonacci", [len(fibonacci(a))/fibonacci(a)[-1] for a in range(10,total,jump)])
#Calling render to 'print' the chart
line.render()
