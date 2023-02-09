# 선형 검색 알고리즘 -보초법

from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)  # seq를 복사
    a.append(key)  # 보초 key를 추가

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i


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
