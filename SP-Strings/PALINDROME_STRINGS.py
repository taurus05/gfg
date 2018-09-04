t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print('Yes') if s[::-1] == s[:] else print('No')
