# cook your dish here
for _ in range(int(input())):
    c, n, k = map(int, input().split())
    list_n = []

    for i in range(n):
        s, e = map(int, input().split())
        list_n.append([s, e])

    list_n.sort(key=lambda x: (x[0], x[1]))

    # print(list_n)
    if k == 0:
        curr_max = 0
        last_end = 0
        last_start = 0
        overlapping = False
        for i in range(n):
            if i == 0:
                last_start = list_n[i][0]
                last_end = list_n[i][1]
                curr_max = max(curr_max, last_start - 1)
            else:
                curr_start = list_n[i][0]
                curr_end = list_n[i][1]

                if curr_start <= last_end:
                    overlapping = True
                    break
                else:
                    curr_max = max(curr_max, curr_start - last_end - 1)
                    last_start = list_n[i][0]
                    last_end = curr_end
        if overlapping:
            print("Bad")
        else:
            print("Good")
    else:
        curr_max = 0
        last_end = 0
        last_start = 0
        overlapping = False
        double_overlap = False
        over_lap_length = 0
        over_lap_length_2 = 0
        change = 0
        for i in range(n):
            if i == 0:
                last_start = list_n[i][0]
                last_end = list_n[i][1]
                curr_max = max(curr_max, last_start - 1)
            else:
                curr_start = list_n[i][0]
                curr_end = list_n[i][1]

                if curr_start <= last_end:
                    if overlapping:
                        double_overlap = True
                        break
                    overlapping = True
                    over_lap_length = curr_end - curr_start + 1
                    over_lap_length_2 = last_end - last_start + 1
                    change = i
                    
                else:
                    curr_max = max(curr_max, curr_start - last_end - 1)
                    last_start = list_n[i][0]
                    last_end = curr_end

        if not overlapping:
            print("Good")
            continue
        elif (not double_overlap) and curr_max >= over_lap_length:
            print("Good")
            continue

        curr_max = 0
        last_end = 0
        last_start = 0
        overlapping = False
        for i in range(n):
            if i == 0:
                last_start = list_n[i][0]
                last_end = list_n[i][1]
                curr_max = max(curr_max, last_start - 1)
            elif i != change - 1:
                curr_start = list_n[i][0]
                curr_end = list_n[i][1]

                if curr_start <= last_end:
                    overlapping = True
                    break
                else:
                    curr_max = max(curr_max, curr_start - last_end - 1)
                    last_start = list_n[i][0]
                    last_end = curr_end

        if (not overlapping) and curr_max >= over_lap_length_2:
            print("Good")
            continue


        print("Bad")