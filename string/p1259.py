# 1

while True:

    n = input()

    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')

# 2

while True:

    n = input()

    if n == '0':
        break

    answer = ''
    rst = []

    for i in range(len(n) - 1, -1, -1):
        rst.append(n[i])

    if n == answer.join(rst):
        print('yes')
    else:
        print('no')
