arr = []
def next_alive(i,le):
    global arr
    if arr[i % le] != -1:
        return i
    return next_alive(arr,i+1,le)

def killer(i,k,le,count):
    global arr
    if count == le-1:
        return
    else:
        count += 1
        if i == 0:
            i = i + (k-1)
            i = i % le
            if arr[i] == -1:
                i = next_alive(i,le)
            arr[i] = -1
        else:
            i = i + k
            i = i % le
            if arr[i] == -1:
                i = next_alive(i,le)
            arr[i] = -1
        killer(i,k,le,count)


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = [i for i in range(1,n+1)]
