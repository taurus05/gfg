t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    group_size = int(input())
    new_arr = []
    for j in range(0, len(arr), group_size):
        new_arr += list(arr[j:j+group_size])[::-1]
    print(new_arr)
