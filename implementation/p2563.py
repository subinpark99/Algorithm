board = [[0] * 100 for i in range(100)]
rst = 0
for i in range(int(input())):
    n, m = map(int, input().split())

    for col in range(n, n + 10):
        for row in range(m, m + 10):
            board[col][row] = 1

for i in board:
    rst += i.count(1)

print(rst)
