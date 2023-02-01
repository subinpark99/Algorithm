# a부터 b까지 정수 합 구하기 1

a = int(input('정수 a값: '))
b = int(input('정수 b값: '))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b + 1):
    if i < b:
        print(f'{i} +', end=' ')  # 합을 구하는 과정 출력
    else:
        print(f'{i} =', end=' ')
    sum += i

print(sum)
