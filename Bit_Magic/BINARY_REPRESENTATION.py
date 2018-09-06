t = int(input())
for i in range(t):
    arr = []
    bit = 0
    n = int(input())
    while n>0:
        bit = n%2
        n = n//2
        arr.append(bit)
    arr.reverse()
    # arr = [0]*(14-len(arr)) + arr
    print(''.join(str(i) for i in arr))
