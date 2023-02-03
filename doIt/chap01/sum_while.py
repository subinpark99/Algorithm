# 1부터 n까지 정수 합(while문)

n = int(input('n값 입력: '))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f'정수 합은 {sum}임')
