N=int(input())
interval_list=[]
for i in range(N):
    interval=list(map(int,input().split()))
    interval_list.append(interval)
interval_list.sort(reverse = True)
def set(N,interval_list):
    if interval_list==[]:
        return 0
    