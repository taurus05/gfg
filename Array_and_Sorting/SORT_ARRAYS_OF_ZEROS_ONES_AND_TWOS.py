t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr0 = []
    arr1 = []
    arr2 = []
    for i in arr:
        if i == 0:
            arr0.append(i)
        elif i == 1:
            arr1.append(i)
        elif i == 2:
            arr2.append(i)
    print(*arr0,*arr1,*arr2)
