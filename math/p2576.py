rst = []
for i in range(7):
    n = int(input())

    if n % 2 != 0:
        rst.append(n)
if len(rst) == 0:
    print(-1)
else:
    print(sum(rst), min(rst), sep='\n')
