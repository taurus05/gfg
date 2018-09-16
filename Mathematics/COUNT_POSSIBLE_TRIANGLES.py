from collections import defaultdict
from math import factorial,ceil
t = int(input())
for i in range(t):
    d = defaultdict(int)
    n = int(input())
    arr = map(int,input().split())
    for i in arr:
        d[i] += 1
    count = 0
    dl = list(d.keys())
    for x in range(len(dl)):
        for y in range(x+1,len(dl)):
            for z in range(y+1,len(dl)):
                if dl[x] + dl[y] > dl[z]:
                    count += d[dl[x]]*d[dl[y]]*d[dl[z]]
    print(count)
