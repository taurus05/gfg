def sieve(n):
    temp = [1]*(n+1)
    temp[0], temp[1] = 0, 0
    arr = []
    i = 2
    while i*i < n+1:
        if i == 2 or temp[i] == 1:
            for x in range(i*2, n+1, i):
                temp[x] = 0
        i+= 1
    for i in range(len(temp)):
        if temp[i] == 1:
            arr.append(i)
    return arr

t = int(input())
for i in range(t):
    n = int(input())
    print(*sieve(n))
