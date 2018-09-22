t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for x in range(n+1):
        if '4' in list(str(x)):
            count += 1
    print(count)
