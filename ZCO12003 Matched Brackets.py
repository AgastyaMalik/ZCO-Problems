n = int(input())
sequence = list(map(int, input().split()))
maxr = 0  # Maximum symbols between () brackets
maxs = 0  # Maximum symbols between [] brackets
rbrac = []  # Stack for () brackets
sbrac = []  # Stack for [] brackets
altdepth = []  # Stack for alternating depth
maxaltdepth = 0  # Maximum alternating depth
current_depth = 0  # Current alternating depth

for i in range(n):
    if sequence[i] == 1:  # Opening (
        rbrac.append(i)
        if not altdepth or altdepth[-1] == ']' :
            current_depth += 1
        altdepth.append('(')
    elif sequence[i] == 2:  # Closing )
        maxr = max(maxr, i - rbrac.pop() + 1)
        if altdepth.pop() == '(':
            if not altdepth or altdepth[-1] == ']':
                maxaltdepth = max(maxaltdepth, current_depth)
                current_depth -= 1
    elif sequence[i] == 3:  # Opening [
        sbrac.append(i)
        if not altdepth or altdepth[-1] == '(':
            current_depth += 1
        altdepth.append('[')
    elif sequence[i] == 4:  # Closing ]
        maxs = max(maxs, i - sbrac.pop() + 1)
        if altdepth.pop() == '[':
            if not altdepth or altdepth[-1] == '(':
                maxaltdepth = max(maxaltdepth, current_depth)
                current_depth -= 1

print(maxaltdepth, maxr, maxs)