{
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        x=int(input())
        print (bin_search(arr, 0, 0, x))
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function
#Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
def bin_search(arr, left, high, key):
    if high == 0 and arr[high] != key:
        high = len(arr)-1
    mid = (left+high)//2
    if arr[mid] == key:
        return mid
    if left >= high and arr[mid]!= key:
        return -1
    elif arr[mid] > key:
        return bin_search(arr, left, mid-1, key)
    elif arr[mid] < key:
        return bin_search(arr, mid+1, high, key)
    return
