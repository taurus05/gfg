from functools import reduce
t = int(input())
for i in range(t):
    n = int(input())
    num = reduce(lambda x,y : x^y,map(int,input().split()))
    print(num)
    
