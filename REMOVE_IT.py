count = 0
for i in range(100000,500001):
    if sum(map(int,list(str(i)))) == 5:
        count += 1
print(count)
