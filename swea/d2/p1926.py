num_list = list(map(str, range(1, int(input()) + 1)))
arr = []

for i in num_list:
    arr = list(i)
    cnt = 0
    temp = ""

    for j in arr:
        if j == '3' or j == '6' or j == '9':
            cnt += 1
    if cnt == 0:
        print(i, end=" ")
    else:
        for x in range(cnt):
            temp += "-"
            print(temp, end=" ")
