# cook your dish here
n,m=map(int,input().split())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
dp=[[0 for i in range(m+1)]for j in range(n+1)]
for i in range(1, n + 1):
        for j in range(1, m+ 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + (l[i-1][j-1] == 0)
q=int(input())
for i in range(q):
    a,b,c,d=map(int,input().split())
    ans=dp[c][d]-dp[a-1][d]-dp[c][b-1]+dp[a-1][b-1]
    if ans:
        print(0)
    else:
        print(1)