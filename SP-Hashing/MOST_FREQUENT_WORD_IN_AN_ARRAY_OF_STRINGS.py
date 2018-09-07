from collections import defaultdict
t = int(input())
for i in range(t):
    d = defaultdict(int)
    _ = int(input())
    words = input().split()
    for word in words:
        d[word] += 1
    print(sorted(d.items(),key = lambda x: (-x[1],x[0]))[0][0])
