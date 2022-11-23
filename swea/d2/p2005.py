for tc in range(int(input())):
    N = int(input())
    result = [[1] for _ in range(N)]

    for i in range(1, N):
        if i == 1:
            result[i].append(1)
            continue
        for j in range(1, i):
            result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        result[i].append(1)

    for i in result:
        if len(i) == 1:
            print('#{}\n{}'.format(tc + 1, *i))
        else:
            print(*i)
