# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    
    ans = 0

    s = 0
    i = 1
    down = True
    prev_s = -1
    prev_v = -1
    prev_i = -1
    while i < len(l):
        down = not down

        if l[i] == l[i-1]:
            if l[i] != prev_v:
                prev_v = l[i]
                prev_i = i - 1
        elif (down == True and l[i] < l[i-1]) or (down == False and l[i] > l[i-1]):
            prev_v = -1
            prev_i = -1
            pass
        else:
            down = not down

            if prev_s != -1:
                ans = max(ans, i - prev_s + 1)
            else:
                ans = max(ans, i - prev_s)
            prev_s = s

            if l[i - 1] == prev_v:
                if l[i] < prev_v:
                    if (i - prev_i) % 2 == 0:
                        s = prev_i
                    else:
                        s = prev_i+1
                else:
                    if (i - prev_i) % 2 == 0:
                        s = prev_i+1
                    else:
                        s = prev_i
            else:
                if l[i] < l[i-1]:
                    s = i
                else:
                    s = i - 1
        i += 1
    if prev_s != -1:
        ans = max(ans, i - prev_s + 1)
    ans = max(ans, i - s + 1)

    print(ans)