t = int(input())
for i in range(t):
    n = int(input())
    i = 0
    while pow(2,i) < n:
        i += 1
    if pow(2,i) == n:
        print('YES')
    else:
        print('NO')
    
