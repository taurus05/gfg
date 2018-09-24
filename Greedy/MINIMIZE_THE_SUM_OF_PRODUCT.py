from functools import reduce
t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr1.sort()
    arr2.sort(reverse=True)
    prod = reduce(lambda x,y : x+y,map(lambda x, y: x*y, zip(arr1, arr2)))
    print(prod)
