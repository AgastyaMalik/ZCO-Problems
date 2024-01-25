M = int(input()) # number of books
l = list(map(int,input().split()))
arr = []
N = int(input())
for i in range(N):
    ind = int(input()) - 1
    
    arr.append(l[ind])
    l.pop(ind)
for i in arr:
    print(i,end="\n")
