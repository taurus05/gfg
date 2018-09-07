def count_bits(n):
    arr = []
    while n>0:
        bit = n%2
        n = n//2
        arr.append(bit)
    return arr.count(1)

t = int(input())
for _ in range(t):
    n = int(input())
    tol_bits = 0
    for i in range(1,n+1):
        tol_bits += count_bits(i)
    print(tol_bits)
