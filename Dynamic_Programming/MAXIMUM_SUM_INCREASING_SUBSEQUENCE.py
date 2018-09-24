t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sums = []
    i = 0
    while i < n:
        j = i+1
        rslt = arr[i]
        while j < n-1:
            if arr[i] <= arr[j]:
                rslt += arr[j]
                if arr[j+1] < arr[j]:
                    print("if arr[j+1] < arr[j]:")
                    sums.append(rslt)
                    rslt = arr[i]
            j += 1
        if j == n-1 and arr[j-1] > arr[j]:
            print("if j == n-1 and arr[j-1] > arr[j]:")
            if arr[j] > arr[i]:
                sums.append(arr[i]+arr[j])
            else:
                sums.append(arr[i])
        elif j == n-1 and arr[j-1] <= arr[j]:
            print("elif j == n-1 and arr[j-1] <= arr[j]:")
            sums.append(rslt+arr[j])
        i += 1
    print(sums)
    print(arr)
