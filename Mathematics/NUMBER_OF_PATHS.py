count = 0
n = 0
m = 0
def paths(s,e):
    global count
    global n
    global m
    if s == n-1 and e == m-1:
        count += 1
    else:
        if s < n:
            paths(s+1,e)
        if e < m:
            paths(s,e+1)

t = int(input())
for i in range(t):
    count = 0
    n, m = map(int,input().split())
    paths(0,0)
    print(count)
    
