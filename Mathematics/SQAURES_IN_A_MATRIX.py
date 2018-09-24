# time complexity O(n)

t = int(input())
for i in range(t):
    m, n = map(int, input().split())
    tol = 0
    for x in range(1,min(m,n)+1):
        tol += (((m-x)+1)*((n-x)+1))
                break
    print(tol)
