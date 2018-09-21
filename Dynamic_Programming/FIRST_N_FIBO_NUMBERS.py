t = int(input())
for i in range(t):
    n = int(input())
    a = 1
    b = 1
    p = 0
    while p < n:
        print(a,end=' ')
        a, b = b, a+b
        p+= 1
    print()
