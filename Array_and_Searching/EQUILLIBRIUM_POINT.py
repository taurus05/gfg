t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = False
    pos = None
    if len(arr) == 1:
        print(1)
    else:
        tarr = arr[::-1]
        for i in range(1,n):
            arr[i] += arr[i-1]
        for i in range(1,n):
            tarr[i] += tarr[i-1]
            if tarr[i] == arr[n-i-1]:
                flag = True
                pos = n-i
                break
        if flag:
            print(pos)
        else:
            print(-1)
