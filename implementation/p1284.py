while True:
    cnt = 0
    a = 0
    n = list(map(int, input()))
    if n[0] == 0:
        break
    for i in n:
        if i == 1:
            cnt += 2
        elif i == 0:
            cnt += 4
        else:
            cnt += 3

    for i in n:
        a = len(n) + 1

    print(cnt + a)
