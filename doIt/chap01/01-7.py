# n까지의 정수 합 (for문)

n = int(input('정수 n값 입력: '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'정수 합은 {sum}임')
