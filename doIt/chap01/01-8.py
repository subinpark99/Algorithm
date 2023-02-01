# a부터 b까지의 정수 합 구하기

a = int(input('a값: '))
b = int(input('b값: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'정수 합은 {sum}임')
