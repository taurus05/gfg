class Stack(object):
    def __init__(self):
        self.top = -1
        self.li = []

    def push(self,val):
        self.top += 1
        self.li.append(val)

    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.li.pop(-1)
        else:
            return 0

    def __len__(self):
        return len(self.li)

t = int(input())
for i in range(t):
    n = list(input())
    flag = True
    stck = Stack()
    if len(n) == 1:
        flag = False
    for i in n:
        if i =='[' or i == '(' or i == '{':
            stck.push(i)
        elif i == ']':
            top = stck.pop()
            if top != '[':
                flag = False
                break
        elif i == ')':
            top = stck.pop()
            if top != '(':
                flag = False
                break
        elif i == '}':
            top = stck.pop()
            if top != '{':
                flag = False
                break

    if flag and len(stck) == 0:
        print('balanced')
    else:
        print('not balanced')
