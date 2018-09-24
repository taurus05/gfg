t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    odd = list(filter(lambda x : x%2 != 0,arr))
    even = list(filter(lambda x : x%2 ==0 ,arr))
    print(*sorted(odd,reverse=True), *sorted(even,reverse=False),sep=' ')
