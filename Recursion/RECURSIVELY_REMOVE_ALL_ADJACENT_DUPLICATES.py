# best problem of the week!!!
# This approach is completly recursive
# Performs multiple rounds of check unless and until the string is completly duplicate free


def checker(s,i,le):
    if len(s) == 1:
        return False
    if i == le-1:
        if s[i-1] == s[i]:
            return True
        else:
            return False
    else:
        if i < le-1 and s[i] == s[i+1]:
            return True    # True will call the function again
        else:
            if i < le - 1:
                return checker(s,i+1,le)
            else:
                return False

def caller(string):
    global arr
    # print(string,'inside caller')
    cond = checker(string,0,len(string))
    if cond:
        arr = []
        # print(string,'inside caller if ')
        fun(string,0,0,len(string))
        return caller(''.join(i for i in arr))
    else:
        if not arr:
            # print(string,'inside caller else -> if')
            return string
        else:
            # print(string,'inside caller else -> else')
            return ''.join(i for i in arr)


def depth(s,i,count,le):
    if i == le-1:
        return 1
    else:
        if s[i] == s[i+1]:
            # print(s,i,count,'inside depth if')
            count = depth(s,i+1,count+1,le)
        # else:
            # print(s,i,count,'inside depth else')
    return count

def fun(s,i,count,le):
    global arr
    if i == le-1:
        # print(s,i,count,'inside fun if')
        if s[i-1] != s[i]:
            arr.append(s[i])
        return

    else:
        if s[i] == s[i+1]:
            # print(s,i,count,'inside fun else -> if')
            deep = depth(s,i,count+1,le)
            return fun(s,i+deep,0,le)
        else:
            arr.append(s[i])
            # print(s,i,count,'inside fun else -> else')
            return fun(s,i+1,0,le)

t = int(input())
for i in range(t):
    arr = []
    s = input()
    print(caller(s))
