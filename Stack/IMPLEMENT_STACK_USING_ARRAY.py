t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    stack = []
    i = 0
    while i < len(arr):
        if arr[i] == 1:
            stack.append(arr[i+1])
            i+=2
        elif arr[i] == 2:
            stack.remove(stack[-1])
            i+=1

    print(stack,sep=' ')
