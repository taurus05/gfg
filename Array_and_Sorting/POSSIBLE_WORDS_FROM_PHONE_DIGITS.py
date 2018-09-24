from functools import reduce
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(str,input().split()))
    mapping = {'2' : ['a','b','c'],'3' : ['d','e','f'],'4' : ['g','h','i'],'5' : ['j','k','l'],'6' : ['m','n','o'], '7' : ['p','q','r','s'], '8' : ['t','u','v'], '9' : ['w','x','y','z']}
    arr = [ mapping[i] for i in arr ]
    vals = reduce(lambda x,y : [i+j for i in x for j in y], arr)
    print(*vals)
