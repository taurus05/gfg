 t = int(input())
for i in range(t):
    n = int(input())
    count = 2
    while n!= 2:
        if n%2 == 0:
            n = n//2
        else:
            n = n - 1
        count += 1
    print(count)
