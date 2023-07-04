while True:
    s = input()
    cnt = 0
    if s == '#':
        break
    for i in s:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
