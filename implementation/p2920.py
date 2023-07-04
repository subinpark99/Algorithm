num = list(map(int, input().split()))

a, b = [], []
for i in range(1, 9):
    a.append(i)

for i in range(8, 0, -1):
    b.append(i)

if num == a:
    print('ascending')

elif num == b:
    print('descending')
else:
    print('mixed')
