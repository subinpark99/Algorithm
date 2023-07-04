a = int(input())
b = int(input())
c = int(input())
rst = list(str(a * b * c))

for i in range(0, 10):
    print(rst.count(str(i)))
