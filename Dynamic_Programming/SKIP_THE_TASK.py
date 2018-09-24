t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    i = 0
    rslt = 0
    while i<n:
        if i+1 < n:
            if arr[i] < arr[i+1]:
                rslt += arr[i]
                if i+2 < n and (arr[i+2] > arr[i+1]):
                    i += 2
            else:
                rslt += arr[i+1]
                i += 1
        i += 1
    print(rslt)
