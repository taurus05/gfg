t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    initial = (n-1)//2
    new_arr = arr[:]
    for i in range(n):
        if i%2 == 0:
            initial -= i
        else:
            initial += i
        new_arr[initial] = arr[i]
    print(*new_arr)
