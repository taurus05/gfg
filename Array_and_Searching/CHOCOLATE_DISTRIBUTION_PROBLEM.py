t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    arr = sorted(arr)
    # We need to search in all the groups to obtain the minimum difference
    grps = len(arr) - m + 1
    min_diff = max(arr)
    beg_index = None
    end_index = None
    for i in range(grps):
        if (arr[i+m-1] - arr[i]) < min_diff:
            beg_index = i
            end_index = i+m-1
            min_diff = arr[i+m-1] - arr[i]
    print(arr[end_index] - arr[beg_index])
