def sieve():
    arr = [True]*(n+1)
    arr[0], arr[1] = False, False
    i = 2
    while i*i < len(arr):
        if i == 2 or arr[i] == True:
            for x in range(2*i, len(arr),i):
                arr[x] = False
        i += 1
    tol = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            tol += i
    return tol

t = int(input())
for i in range(t):
    n = int(input())
    print(sieve())
