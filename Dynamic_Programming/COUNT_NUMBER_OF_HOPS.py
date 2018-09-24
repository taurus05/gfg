def climb(n):
    global count
    arr = [1,2,4]
    if n > 3:
        for i in range(3,n):
            arr.append(sum(arr[i-3:i]))
        return arr[-1]
    else:
        return arr[n-1]

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    print(climb(n))
