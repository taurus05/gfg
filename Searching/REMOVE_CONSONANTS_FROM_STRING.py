import re
t = int(input())
for i in range(t):
    n = list(map(str,input().split(' ')))
    temp = []
    count = 0
    for j in range(len(n)):
        if not re.findall(r'[aeiouAEIOU]', n[j]):
            count += 1
        temp.append(re.sub(r'[^aeiouAEIOU ]', r'', n[j]))
    if count == len(n):
        print('No Vowel')
    else:
        print(*temp)
