from collections import deque

for _ in range(int(input())):
    s = input()
    n = int(int(input()))
    nst = input()[1:-1].split(',')
    rst = deque(nst)

    flag = False
    reverse = 0
    if n == 0:
        rst = []

    for i in s:
        if i == 'R':
            reverse += 1

        else:
            if rst:
                if reverse % 2 == 0:
                    rst.popleft()
                else:
                    rst.pop()
            else:
                print('error')
                flag = True
                break

    if not flag:
        if reverse % 2 == 1:
            rst.reverse()
        print('[' + ','.join(rst) + ']')
