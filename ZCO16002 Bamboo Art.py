ai = [int(i) for i in input().split()]
n = ai.pop(0)
ai = sorted(ai)
se = set(ai)
ans = 1
for i in range(1, n):
    for j in range(i):
        dif = ai[i] - ai[j]
        tot = 2
        x = ai[i] + dif
        while x in se:
            tot += 1
            x += dif
        ans = max(ans, tot)
print(ans)