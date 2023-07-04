alp = '0abcdefghijklmnopqrstuvwxyz'

rst, cnt = 0, 0
num = int(input())
char = input()

for i in char:
    rst += (alp.index(i)) * 31 ** cnt
    cnt += 1
print(rst % 1234567891)
