# 이진 검색 알고리즘

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1


if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:  # 바로 직전 원소보다 큰 값 입력
                break
    keys = int(input('검색할 값 입력: '))

    idx = bin_search(x, keys)

    if idx == -1:
        print('원소 존재 x')
    else:
        print(f'검색값은 x[{idx}]에 있음')
