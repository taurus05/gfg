#code
from math import gcd
from functools import reduce
t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))
    final = reduce(lambda x, y: gcd(x,y), li)
    print(final)
