from collections import defaultdict
t = int(input())
for i in range(t):
    n = int(input())
    words = input().split()
    d = defaultdict(list)
    word0 = sorted(list(words[0]))
    for word in words:
        if sorted(list(word)) == word0:
            d[''.join(x for x in word0)].append(word)
        else:
            d[''.join(x for x in sorted(list(word)))].append(word)
    for i in sorted(d.items(),key = lambda x:len(x[1])):
        print(len(i[1]),end = ' ')
    print()
