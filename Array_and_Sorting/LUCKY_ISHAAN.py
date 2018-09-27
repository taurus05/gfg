#code
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    temp = [0]*136
    count = 0
    for num in arr:
        index = sum([int(x) for x in list(str(num))])
        if temp[index] == 0:
            temp[index] = 1
            count += 1
    print(count)

    
