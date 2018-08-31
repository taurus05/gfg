def left_most(arr, left, key):
    while left > 0 and arr[left] == key:
        if arr[left] == arr[left-1]:
            left -= 1
        else:
            break
    return left

def high_most(arr, high, key):
    while high < len(arr)-1 and arr[high] == key:
        if arr[high] == arr[high+1]:
            high += 1
        else:
            break
    return high

def bin_search(arr, left, high, key):
    mid = (left+high)//2
    if arr[mid] == key:
        return [left_most(arr, mid, key), high_most(arr, mid, key)]
    if left >= high and arr[mid]!= key:
        return [-1]
    elif arr[mid] > key:
        return bin_search(arr, left, mid-1, key)
    elif arr[mid] < key:
        return bin_search(arr, mid+1, high, key)
    return



t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int, input().strip().split(' ')))
    x=int(input())
    print (*bin_search(arr, 0, n-1, x))
