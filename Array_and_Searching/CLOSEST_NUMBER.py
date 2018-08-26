def bsearch(beg, mid, end, ele ,arr):
    while beg < end:
        mid = (beg+end)//2
        if arr[mid] == ele:
            return arr[mid+1]
        else:
            if (abs(arr[mid] - ele) > abs(arr[mid-1] - ele)) and (abs(arr[mid] - ele ) < abs(arr[mid+1] - ele)):
                end = mid+1
            elif (abs(arr[mid] - ele) < abs(arr[mid-1] - ele)) and (abs(arr[mid] - ele ) > abs(arr[mid+1] - ele)):
                beg = mid-1
            elif (abs(arr[mid] - ele) < abs(arr[mid-1] - ele)) and (abs(arr[mid] - ele ) < abs(arr[mid+1] - ele)):
                return arr[mid]
            elif (abs(arr[mid] - ele) < abs(arr[mid-1] - ele)) and (abs(arr[mid] - ele ) <= abs(arr[mid+1] - ele)):
                return arr[mid+1]



t = int(input())
for i in range(t):
    n, ele  = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = set(arr)
    # using modified binary search to find the element closest to the given element
    beg = 0
    end = len(arr)-1
    mid = None
    print(bsearch(beg, mid, end, ele ,list(arr)))
