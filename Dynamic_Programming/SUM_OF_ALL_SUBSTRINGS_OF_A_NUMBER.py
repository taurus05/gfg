t = int(input())
for i in range(t):
     n = int(input())
     li = str(n)
     s = 0
     for i in range(0,len(li)):
         j = len(li) - 1
         while j >= i:
             s += int(li[i:j+1])
             j -= 1
     print(s)
