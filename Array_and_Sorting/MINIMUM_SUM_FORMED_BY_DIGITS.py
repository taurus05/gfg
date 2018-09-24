t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    n1 = []
    n2 = []
    if n == 1:
        print(arr[0])
    else:
        for i in range(0,n,2):
            n1.append(arr[i])
            if i+1 < n:
                n2.append(arr[i+1])
        n1 = int(''.join(str(x) for x in n1))
        n2 = int(''.join(str(x) for x in n2))
        print(n1+n2)
