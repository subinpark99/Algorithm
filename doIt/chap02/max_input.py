# 배열 원소의 최댓값을 구해서 출력(원소값 입력받음)

from max import max_of

number = 0
x = []

while True:
    s = input(f'x[{number}]값 입력: ')
    if s == 'End':
        break
    x.append(int(s))  # 배열의 맨 끝에 추가
    number += 1

print(f'{number}개를 입력함')
print(f'최댓값은 {max_of(x)}임')
