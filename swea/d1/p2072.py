T = int(input())

for i in range(1, T + 1):
    list_num = list(map(int, input().split()))
    answer = 0
    for num in list_num:
        if num % 2 != 0:
            answer += num
    print("#" + str(i) + " " + str(answer))
