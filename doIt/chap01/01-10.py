# a부터 b까지 정수 합 구하기 2

a = int(input('정수 a값: '))
b = int(input('정수 b값: '))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b):
    print(f'{i} + ', end=' ')
    sum += i

print(f'{b} = ', end=' ')
sum += b
print(sum)
