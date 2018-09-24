count = 0
def fun(m,n,x):
    global count
    if x == 0 and n == 0:
        print("if x == 0 and n == 0:")
        count += 1
        return
    else:
        i = 1
        while(i<=m):
            print("for i in range(1,m+1):")
            return fun(m,n-1,x-i)
            i += 1

t = int(input())
for i in range(t):
    m,n,x = map(int,input().split())
    count = 0
    fun(m,n,x)
    print(count)
