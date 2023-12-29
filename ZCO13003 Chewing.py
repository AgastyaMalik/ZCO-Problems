N,K = map(int,input().split())
quotients = list(map(int, input().split()))
quotients.sort()
count = 0
left_ptr = 0
right_ptr = N-1
while right_ptr>left_ptr:
    if quotients[left_ptr]+quotients[right_ptr]<K:
        count+= right_ptr -left_ptr
        left_ptr+=1
        
    else:
        right_ptr-=1
print(count)