t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())
    arr.sort(reverse=True)
    rslt = 0
    i = 0
    while i < n:
        if i + 1 < n:
            if arr[i] - arr[i+1] < k:
                rslt += (arr[i] + arr[i+1])
                i += 1
        i += 1
    print(rslt)
