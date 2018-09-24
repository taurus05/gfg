fibo = []
t = int(input())
for i in range(t):
    n = int(input())
    a = 0
    b = 1
    s = 0
    while b <=n:
        if b%2 == 0:
            s = s+b
        a,b = b, a+b
    print(s)
