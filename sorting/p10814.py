answer = []
for i in range(int(input())):
    answer.append(list(map(str, input().split())))

answer.sort(key=lambda x: int(x[0]))

for i in range(len(answer)):
    print(answer[i][0], answer[i][1])
