# *를 n개 출력하되 w개마다 줄바꿈 2

n = int(input('몇 개 출력? '))
w = int(input('몇 개마다 줄바꿈? '))

for _ in range(n // w):
    print('*' * w)

rest = n % w

if rest:
    print('*' * rest)  # n이 w의 배수가 아닌 경우 마지막 행 출력
