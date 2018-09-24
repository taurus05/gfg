t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    temp = [1 for x in range(n-1) for y in range(x+1,n) if x*arr[x] > y*arr[y]]
    print(sum(temp))
