n = int(input())
x = list(map(int, input().split()))
m = int(input())
y = list(map(int, input().split()))
s = dict()

for i in x:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1

for i in range(m):
    if y[i] in s:
        print(s[y[i]], end=' ')
    else:
        print(0, end=' ')
