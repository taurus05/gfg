t = int(input())
for i in range(t):
    n, k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    lens = []
    for i in range(n-k+1):
        lens.append(len(set(arr[i:i+k])))
    print(*lens)
