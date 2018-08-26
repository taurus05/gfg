# naive approach uses worst case time complexity of O(n^2)
# Better approach uses O(n) time complexity

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    rmax = None
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        if i == len(arr)-1:
            new_arr.append(arr[i])
            rmax = arr[i]
        else:
            if arr[i] > rmax:
                new_arr.append(arr[i])
                rmax = arr[i]
    new_arr.reverse()
    print(new_arr)
