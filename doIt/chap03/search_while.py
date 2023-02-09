# 선형 검색 알고리즘- while 문

from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):  # 검색할 값 못찾고 배열의 맨 끝을 지나감
            return -1
        if a[i] == key:  # 검색할 값과 같은 원소 찾음
            return i
        i += 1


if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    keys = int(input('검색할 값 입력: '))

    idx = seq_search(x, keys)

    if idx == -1:
        print('원소 존재 x')
    else:
        print(f'검색값은 x[{idx}]에 있음')
