i, j = map(int, input().split())
n = int(input())

j += n

if j >= 60:
    i += j // 60
    j = j % 60
else:
    j = j
if i >= 24:
    i -= 24
print(i, j)
