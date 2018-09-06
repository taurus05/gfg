t = int(input())
for i in range(t):
    arr = []
    bit = 0
    n = int(input())
    if n == 0:
        print(0)
    else:
        while n>0:
            bit = n%2
            n = n//2
            arr.append(bit)
        for b in range(len(arr)):
            if arr[b] == 1:
                print(b+1)
                break
