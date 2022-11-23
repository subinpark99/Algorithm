T = int(input())

for i in range(1, T + 1):
    num_list = list(map(int, input().split()))
    avg = sum(num_list) / 10

    print("#" + str(i) + " " + str(round(avg)))
