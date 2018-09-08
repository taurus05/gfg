def is_unique(num):
    arr = []
    while num > 0:
        arr.append(num%10)
        num = num//10
    if len(arr) == len(set(arr)):
        return True
    else:
        return False

t = int(input())
for i in range(t):
    m, n = map(int,input().split())
    for ele in range(m,n+1):
        if is_unique(ele):
            print(ele,end=" ")
    print()
