def find_floor(arr, low, high, key):
    if key < arr[0]:
        return -1
    if key > arr[high]:
        return high
    while low < high:
        mid = (low+high)//2
        if arr[mid] == key or (arr[mid] < key and arr[mid+1] > key):
            return mid
        elif arr[mid] > key and arr[mid-1] <= key:
            return mid-1
        elif arr[mid] < key and arr[mid+1] >= key:
            return mid+1
        elif arr[mid] < key and arr[mid+1] < key:
            low = mid+1
        elif arr[mid] > key and arr[mid-1]> key:
            high = mid-1

t = int(input())
for i in range(t):
    n, num = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(find_floor(arr, 0, n-1, num))
