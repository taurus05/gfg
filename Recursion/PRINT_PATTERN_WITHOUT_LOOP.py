def fun(num,flag):
    global n
    if num == n:
        print(num,end=' ')
        return
    else:
        if not flag:
            if num > 0:
                print(num,end=' ')
                fun(num-5,False)
            else:
                print(num,end = ' ')
                fun(num+5,True)
        else:
            print(num,end = ' ')
            fun(num+5,True)


t = int(input())
for i in range(t):
    global n
    flag = False
    n = int(input())
    print(n,end=' ')
    fun(n-5,flag)
    print()
    
