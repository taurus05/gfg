from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    k = int(input())
    d = defaultdict(list)
    count = 0
    for ele1 in range(len(arr)-1):
        for ele2 in range(ele1+1, len(arr)):
            if abs(arr[ele1] - arr[ele2]) == k and ele1 != ele2:
                if [arr[ele1],arr[ele2]] not in d[k] and [arr[ele2],arr[ele1]] not in d[k]:
                    d[k].append([arr[ele1],arr[ele2]])
                    count += 1
    print(count)

    # very high worst case complexity solution
    # complexity is O(n^3)
    # needs some optimization to be perfromed on this.
