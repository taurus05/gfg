# Good problem

t = int(input())
li = [x for x in range(6)] + [0 for x in range(100000)]
for i in range(t):
    n = int(input())
    if li[n] != 0:
        print(li[n])
    else:
        temp = 6
        while temp <= n:
            t2 = temp // 2
            t3 = temp // 3
            t4 = temp // 4
            if t2 + t3 + t4 < temp:
                li[temp] = temp
            else:
                li[temp] = li[t2] + li[t3] + li[t4]
            temp += 1
        print(li[n])
