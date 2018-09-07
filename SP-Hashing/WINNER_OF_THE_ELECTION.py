from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    d = defaultdict(int)
    s = list(input().split())
    for i in s:
        d[i] += 1
    s = sorted(d.items(),key= lambda x : (-x[1],x[0]))
    print(*s[0])
