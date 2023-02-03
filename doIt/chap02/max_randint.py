# 배열 원소의 최댓값을 구해서 출력(원솟값을 난수롤 생성)

import random
from max import max_of

num = int(input('난수 개수 입력: '))
lo = int(input('난수 최솟값 입력: '))
hi = int(input('난수 최댓값 입력: '))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(x)
print(f'최댓값은 {max_of(x)}임')
