t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    num = int(input())
    if arr.count(num):
        print(arr.index(num))
    else:
        print(-1)
