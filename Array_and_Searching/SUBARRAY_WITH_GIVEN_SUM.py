t = int(input())
for i in range(t):
    n, s = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = [0] + arr
    n += 1
    beg, end = 0, 0
    cond = False
    for i in range(1,n):
        arr[i] += arr[i-1]
    while end < n:
        if s == (arr[end] - arr[beg]):
            cond = True
            break
        elif s > (arr[end] - arr[beg]):
            end += 1
        else:
            beg += 1
    if cond:
        print(beg+1, end)
    else:
        print(-1)
