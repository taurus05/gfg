t = int(input())
for i in range(t):
    n, num = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    if arr.count(num):
        print(arr.count(num))
    else:
        print(-1)
