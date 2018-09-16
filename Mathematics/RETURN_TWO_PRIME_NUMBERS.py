def check_prime(n):
    flag = 0
    for i in range(2,n):
        if n%i == 0:
            flag = 1
            break

    if flag:
        return False
    else:
        return True

t = int(input())
for i in range(t):
    n = int(input())
    for i in range(3,n+1):
        if check_prime(i) and check_prime(n-i):
            print(i, n-i, sep= ' ')
            break
