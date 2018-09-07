from collections import defaultdict
t = int(input())
for i in range(t):
    str1 = input()
    str2 = list(set(input()))
    d = defaultdict()
    flag = False
    for i in str2:
        if i in str1:
            d[i] = str1.index(i)
            flag = True
    if flag:
        print(sorted(d.items(), key = lambda x: x[1])[0][0])
    else:
        print('No character present')
