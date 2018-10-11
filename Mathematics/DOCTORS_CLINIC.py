#code
t = int(input())
for i in range(t):
    pat, at = map(int, input().split())
    time = ((pat-1)*10 - (pat-1)*at)
    if time < 0:
        print(0)
    else:
        print(time)
