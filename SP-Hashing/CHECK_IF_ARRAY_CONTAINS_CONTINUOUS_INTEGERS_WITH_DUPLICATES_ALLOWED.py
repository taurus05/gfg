t = int(input())
for i in range(t):
    n = int(input())
    arr = set(map(int,input().split()))
    sn = ((len(arr)/2) * (2*min(arr) + (len(arr)-1)))
    if sn == sum(arr):
        print('Yes')
    else:
        print('No')
