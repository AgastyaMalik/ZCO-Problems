n = int(input())  # number of days data is available
num_of_min = list(map(int, input().split()))

l = [0] * n  # Initialize a list to store the minimum time for each day

# Base cases
l[0] = num_of_min[0]
l[1] = num_of_min[1]
l[2] = num_of_min[2]

for i in range(3, n):  # shortest path to element i
    l[i] = num_of_min[i] + min(l[i-1], l[i-2], l[i-3])

if n < 3:
    print(min(num_of_min))
else:
    print(min(l[n-1], l[n-2], l[n-3]))
