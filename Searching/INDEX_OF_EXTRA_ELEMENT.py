t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    beg = 0
    end = n - 2
    index = None
    while beg < end:
        mid = (beg + end)//2
        if brr[mid] == arr[mid]:
            beg = mid + 1
        else:
            index = mid
            end = mid - 1
    print(index)
