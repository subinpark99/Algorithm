rst = []
for i in range(5):
    rst.append(input())

for i in range(max(len(j) for j in rst)):
    for j in range(5):
        if i < len(rst[j]):
            print(rst[j][i], end='')
