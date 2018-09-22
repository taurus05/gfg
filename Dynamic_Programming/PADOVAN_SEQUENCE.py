# can be solved without adding extra memory overhead
# i.e. instead of storing the values in the memory we can compute the ith value on the go.

t = int(input())
for i in range(t):
    n = int(input())
    p = [1]*3
    pi = 0
    for i in range(3,n+1):
        pi = p[(i-2)] + p[(i-3)]
        p.append(pi)
    print(p[-1])
