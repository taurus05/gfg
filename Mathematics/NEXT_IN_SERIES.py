def is_ap(arr,n):
    flag = False
    d = 0
    for i in range(n-1):
        if d == 0:
            d = arr[i+1] - arr[i]
        else:
            if d == (arr[i+1] - arr[i]):
                flag = True
                break
    if flag:
        return arr[n-1] + d
    else:
        return False

def is_gp(arr,n):
    flag = False
    r = 0
    for i in range(n-1):
        if r == 0:
            if arr[i] == 0:
                break
            else:
                r = (arr[i+1]/arr[i])
        else:
            if arr[i] == 0:
                break
            elif r == (arr[i+1]/arr[i]):
                flag = True
                break
            else:
                break
    if flag:
        return int(arr[n-1]*r)
    else:
        return False

def is_fibo(arr,n):
    flag = False
    a = arr[0]
    b = arr[1]
    if n > 2:
        if a+b == arr[2]:
            flag = True
    else:
        return a+b
    if flag:
        return arr[n-1] + arr[n-2]
    else:
        return False

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if is_ap(arr,n):
        print(is_ap(arr,n)%(10**9 + 7))
    elif is_gp(arr,n):
        print(is_gp(arr,n)%(10**9 + 7))
    elif is_fibo(arr,n):
        print(is_fibo(arr,n)%(10**9 + 7))
    else:
        print(-99999)
