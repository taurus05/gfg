t = int(input())
for i in range(t):
    s = list(input())
    vowels = []
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            vowels.append(s[i])
            s[i] = '*'
    vowels.reverse()
    k = 0
    for i in range(len(s)):
        if s[i] == '*':
            s[i] = vowels[k]
            k += 1
    print(''.join(i for i in s))
