p = input()
n = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
rst = 0

for i in n:
    for j in p:
        if j in i:
            rst += n.index(i) + 3
print(rst)
