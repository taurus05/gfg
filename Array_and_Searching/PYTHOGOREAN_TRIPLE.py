t = int(input())
for i in range(t):
    n = int(input())
    arr =list(map(lambda x : int(x)**2, input().split()))
    arr.sort()
    for c in range(len(arr)-1,1,-1):
        a = 0
        b = c-1
        cond = False
        while a < b:
            if arr[a] + arr[b] == arr[c]:
                cond = True
                break
            elif arr[a] + arr[b] < arr[c]:
                a += 1
            else:
                b = b - 1
        if cond:
            print('Yes')
            break
    if not cond:
        print('No')
            
