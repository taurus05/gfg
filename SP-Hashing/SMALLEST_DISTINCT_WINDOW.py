t = int(input())
for i in range(t):
    s = input()
    distinct = set(s)
    len_dist = len(distinct)
    flag = True
    for x in range(len_dist,len(s)+1):
        if flag:
            for y in range(0,len(s)-x+1):
                if len(set(s[y:y+x])) == len_dist:
                    print(len(s[y:y+x]))
                    flag = False
                    break
        else:
            break
