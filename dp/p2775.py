for _ in range(int(input())):
    k = int(input())
    n = int(input())
    lst = [m for m in range(1, n + 1)]

    for i in range(k):
        for j in range(1, n):
            lst[j] += lst[j - 1]

    print(lst[-1])
