from collections import defaultdict
t = int(input())
for i in range(t):
    s = input()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    if sum(d.values()) == len(set(s)):
        print(1)
    else:
        print(0)
