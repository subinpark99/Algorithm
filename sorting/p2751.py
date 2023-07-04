import sys

rst = []
for i in range(int(input())):
    rst.append(int(sys.stdin.readline()))

for i in sorted(rst):
    sys.stdout.write(str(i) + '\n')
