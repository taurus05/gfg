# need to make the implementation faster

li = []
def find_pal(s):
    global li
    if s[:] not in li and s[:] == s[::-1]:
        li.append(''.join(x for x in s))
        return
    else:
        for i in range(len(s)//2+1):
            if i == 0:
                if s[i] != s[len(s)-1-i]:
                    find_pal(s[:len(s)-i-1])
                    find_pal(s[i+1:])
            else:
                if s[i] != s[len(s)-1-i]:
                    find_pal(s[:len(s)-i])
                    find_pal(s[i:])



t = int(input())
for i in range(t):
    li = []
    s = list(input())
    find_pal(s)
    print(sorted(li,key = lambda x:len(x),reverse=True)[0])
