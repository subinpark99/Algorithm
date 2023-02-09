# seq_search() 함수를 이용하여 실수 검색

from search_while import seq_search

number = 0
x = []

while True:
    s = input(f'x{number}: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

keys = float(input('검색할 값 입력: '))

idx = seq_search(x, keys)
if idx == -1:
    print('원소 존재 x')
else:
    print(f'원소값은 x[{idx}]에 있음')
