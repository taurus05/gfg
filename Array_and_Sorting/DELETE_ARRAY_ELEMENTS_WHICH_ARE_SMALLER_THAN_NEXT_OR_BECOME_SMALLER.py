#code
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    p = 0
    temp = []
    cond = True
    for i in range(n):
        if i > 0 and cond:
            while temp and p < k and temp[-1] < arr[i]:
                temp.pop(-1)
                p += 1
        temp.append(arr[i])
        if k == p:
            cond = False
    print(*temp)

            
