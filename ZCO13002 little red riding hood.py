import sys
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
grid = []
for i in range(n):
    grid.append( list(map(int,input().split())))
charms  = []
safe = set()    
for _ in range(m):
    asa,b,k = map(int,input().split())
    charms.append([asa,b,k])
    asa -= 1
    b -= 1
    x = max(0, asa - k)
    while x < n and x <= asa + k:
        off = abs(x - asa)
        y = max(0, b - k + off)
        while y < n and y <= b + k - off:
            safe.add((x,y))
            y += 1
        x += 1

max_arr = [[-1 for i in range(n)] for j in range(n)]
def func(n,m,arr,safe,i,j):
    global max_arr
    if i<0 or j<0 or i>=n or j>=n or (i,j) not in safe:
        return float("-inf")
    if i==n-1 and j==n-1:
        return arr[i][j]
    if max_arr[i][j] !=-1:
        return max_arr[i][j]
    max_arr[i][j] = arr[i][j] + max(func(n,m,arr,safe,i+1,j),func(n,m,arr,safe,i,j+1))
    return max_arr[i][j]
res = func(n,m,grid,safe,0,0)
if res!=float("-inf"):
    print("YES")
    print(res)
else:
    print("NO")
    