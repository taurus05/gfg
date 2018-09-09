from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    d = defaultdict(int)
    arr1 = map(int,input().split())
    arr2 = map(int, input().split())
    # for i in arr2:
    #     d[i] += 1
    # count = []
    # for x in arr1:
    #     val = 0
    #     for y in d.keys():
    #         if y <= x:
    #             val += d[y]
    #     count.append(val)
    # print(count,sep=',')
    # This is O(n^2)
    # Can achieve O(n) complexity
    hash_map = [0]*100
    for i in arr2:
        hash_map[i] += 1
    for i in range(1,len(hash_map)):
        hash_map[i] = hash_map[i] + hash_map[i-1]
    count = []
    for i in arr1:
        count.append(hash_map[i])
    print(*count,sep=',')
