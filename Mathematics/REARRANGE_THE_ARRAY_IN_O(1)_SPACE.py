t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    temp = []
    for i in range(len(arr)):
        temp.append(arr[arr[i]])
        # arr.pop(arr[i])
    print(*temp,sep=' ')
