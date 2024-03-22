# cook your dish here

t = int(input())



for _ in range(t):

    n = int(input())
    arr = [list(map(int, input().split()))+[i] for i in range(n)]
    l = sorted(arr, key=lambda x:x[0])
    r = sorted(arr, key=lambda x:x[1], reverse=True)
    #print(arr)
    ans = [0 for i in range(n)]
    for i in range(n):
        ans[l[i][-1]] += n-i-1
        ans[r[i][-1]] += n-i-1
    print(*ans)