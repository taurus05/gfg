n = int(input())
arr = list(map(int,input().split()))
val = int(input())
i = 0
j = n-1
diff = 2*max(arr)
a, b = None, None
while i < j:
    if abs(arr[i] + arr[j] - val) < diff:
        diff = abs(arr[i] + arr[j] - val)
        a, b = arr[i], arr[j]
    if (arr[i] + arr[j]) > val:
        j -= 1
    else:
        i += 1
print(a,b)
print(arr)
