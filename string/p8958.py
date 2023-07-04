for i in range(int(input())):
    cnt = 0
    s = 1
    n = input()
    for i in n:
        if i == 'O':
            cnt += s
            s += 1

        else:
            s = 1

    print(cnt)
