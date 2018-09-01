## wrong solution
## do not read this solution!!

t = int(input())
for i in range(t):
    n1, n2 = map(int, input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    num = int(input())
    li = arr[:] + brr[:]
    i = 0
    j = n1 + n2-1
    diff = 2*max(li)
    a, b = None, None
    while i < n1 and j >= n1:
        if abs(li[i] + li[j] - num) < diff:
            diff = abs(li[i] + li[j] - num)
            a, b = li[i], li[j]
        if (li[i] + li[j]) > num :
            if li[i] > li[j] and i > 0:
                i -= 1
            elif li[j] >= li[i]:
                j -= 1
            elif li[i] > li[j] and j > n1:
                j -= 1
        elif (li[i] + li[j]) < num:
            if (i < n1-1 and j > n1) and li[i+1] > li[j-1]:
                j += 1
            elif (i < n1-1 and j > n1) and li[i+1] <= li[j-1]:
                i += 1
        else:
            i += 1
            j -= 1
    print(a,b)
