for i in range(int(input())):
    n = input()
    rst = []

    for j in n:
        if j == '(':
            rst.append(j)
        elif j == ')':
            if len(rst) != 0:
                rst.pop()
            else:
                rst.append(j)
                break

    if len(rst) != 0:
        print("NO")
    else:
        print("YES")
