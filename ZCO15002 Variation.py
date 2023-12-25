x = input().split()
N, K = int(x[0]), int(x[1])
array = input().split()
integers = sorted([int(i) for i in array])

count = 0
left_ptr = 0
right_ptr = 1

while right_ptr < N:
    diff = integers[right_ptr] - integers[left_ptr]
    if diff >= K:
        count += N - right_ptr
        left_ptr += 1
    else:
        right_ptr += 1

print(count)
