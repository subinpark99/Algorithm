for i in range(int(input())):
    s = ""
    a, b = map(str, input().split())
    for j in b:
        s += j * int(a)
    print(s)
