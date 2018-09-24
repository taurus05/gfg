t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    rot = int(input())
    arr = arr[ rot%len(arr) :  ] + arr[ : rot%len(arr) ]
    print(*arr)
