t = int(input())
for i in range(t):
    n, ele  = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    temp = list(map(lambda x : abs(x-ele), arr))
    dmin = min(temp)
    print(arr[len(temp) - 1 - temp[::-1].index(dmin)])
# more effecient implementation using binary search yet to be implemented
