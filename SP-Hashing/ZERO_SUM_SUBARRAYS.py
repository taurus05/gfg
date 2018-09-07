t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(i,n):
            if sum(arr[i:j+1]) == 0:
                count += 1
    print(count)


    # A much better solution exists for the above problem, which uses hash table
    # Complexity of the above solution is O(n^2)
    # using hash tables , it reduces to O(n)
    
