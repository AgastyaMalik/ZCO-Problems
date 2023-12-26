N = int(input())
strengths = list(map(int, input().split()))
strengths.sort()
revenue = 0
for i in range(N):
    revenue += (i * strengths[i] - (N - 1 - i) * strengths[i])
print(revenue)
