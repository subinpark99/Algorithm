# 1부터 n까지 합(n값은 양수만 입력)

while True:
    n = int(input('n값 입력: '))
    if n > 0:
        break  # n이 양수인 경우 무한 루프에서 빠져나옴

sum = 0
i = 1

for i in range(1, n + 1):
    sum += i
    i += 1

print(sum)
