
inp = list(map(int,input().split()))
n,k,arr = inp[0],inp[1],inp[2:]
pairs = [0]*(k+1)
if n<4: print(0)
else:
    tsum = arr[0]+arr[1]
    if tsum<=k: pairs[tsum]=1
    res = 0
    for i in range(2,n-1):
        for j in range(i+1,n):
            x = arr[i]+arr[j]
            if x<=k: res += pairs[k-x]
        for j in range(i):
            x = arr[i]+arr[j]
            if x<=k: pairs[x]+=1
    print(res)