from collections import OrderedDict
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    d = OrderedDict()
    flag = False
    for x in nums:
        if x in d.keys():
            d[x] += 1
        else:
            d[x] = 1
    for i,j in d.items():
        if d[i] == k:
            print(i)
            flag = True
            break
    if not flag:
        print(-1)
