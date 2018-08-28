t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    maxe = max(arr)
    mine = min(arr)
    loc_maxe = arr.index(maxe)
    arr0 = arr[0]
    arrn = arr[n-1]
    if (arr0 < arrn) and (arr0 == mine) and (arrn == maxe):
        print(maxe,1,sep=' ')
    elif (arrn == mine) and (arr0 > arrn) and (arr0 == maxe):
        print(maxe,2,sep=' ')
    elif (arr[loc_maxe - 1] == mine) and (arr0 < arrn):
        print(maxe,3,sep=' ')
    elif (arr[loc_maxe + 1] == mine) and (arr0 > arrn):
        print(maxe,4,sep=' ')
