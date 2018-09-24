## The time limit is exceeding for the problem.
## More effecient solution needed.

from math import sqrt,ceil
def sieve():
    global primes
    arr = []
    for num in range(3,10000001):
        flag = True
        for j in range(2,num):
            if num%j == 0:
                flag = False
                break
        if flag:
            primes.append(num)

primes = [2]
sieve()
print(len(primes))

def is_prime(n):
    global primes
    if n in primes:
        return True
    else:
        if n < primes[-1]:
            return False
        else:
            flag = True
            for i in primes:
                if n%i == 0:
                    flag = False
                    break
            if flag:
                return True
            else:
                return False


t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    for num in range(n+1):
        if num > 2 and is_prime(num):
            for p1 in range(2,num+1):
                if is_prime(p1) and is_prime(num-p1):
                    count += 1
                    break
    print(count)
