t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    new_arr = []
    for i in range(len(arr)):
        if i == len(arr)-1:
            new_arr.append(-1)
        else:
            if arr[i] > arr[i+1]:
                new_arr.append(arr[i+1])
            else:
                new_arr.append(-1)
    print(*new_arr)
