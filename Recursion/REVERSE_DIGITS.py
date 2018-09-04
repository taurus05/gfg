li = []
def rev(num,n):
    global li
    if n == 1:
        li.append(str(num))
    else:
        rev(num%(10**(n-1)), n-1)
        li.append(str(num//(10**(n-1))))

t = int(input())
for i in range(t):
    li = []
    num = int(input())
    rev(num, len(str(num)))
    print(int(''.join(x for x in li)))
