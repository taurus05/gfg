t = int(input())
for i in range(t):
    x, y = map(int,input().split())
    if x == 1:
        if x == y:
            print(1)
        else:
            print(0)
    elif x == y:
        print(1)
    else:
        i = 0
        while pow(x,i) < y:
            i += 1
        if pow(x,i) == y:
            print(1)
        else:
            print(0)
