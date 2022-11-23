T = int(input())

for i in range(1, T + 1):
    day = input()
    year = day[:4]
    month = day[4:6]
    date = day[6:8]

    date_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if 0 < int(month) < 13 and 0 < int(date) <= date_dict[int(month)]:
        print("#" + str(i) + " " + str(year) + "/" + str(month) + "/" + str(date))
    else:
        print("#" + str(i) + " " + str(-1))
