while True:
    n = int(input())
    s = []
    if n == -1:
        break

    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            s.append(i)

    if sum(s) == n:
        m = ' + '.join(str(i) for i in s)
        print(f'{n} = {m}')
    else:
        print(f'{n} is NOT perfect.')
