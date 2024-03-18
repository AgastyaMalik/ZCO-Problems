# cook your dish here
list_n = list(map(int, input().split()))
n = list_n[0]
k = list_n[1]
list_a = list_n[2: 2 + n]
list_b = list_n[2 + n : ]



list_a.sort()
list_b.sort()

#print(list_a)
#print(list_b)

i = 0
min_1 = float('inf')

while i < k:
  if(list_a[-i-1] > list_b[i]):
    i += 1
  else:
    break 

i-=1
if i != -1:
  min_1 = max(max(list_a[:-i-1]), max(list_b[:i + 1]))
  min_2 = max(max(list_a), max(list_b))
  
  min_1 = abs(min_2 + min_1)
  
  #print(min_1)
else:
  min_1 = list_a[-1] + list_b[-1]

i = 0
while i < k:
  if(list_b[-i-1] > list_a[i]):
    i += 1
  else:
    break 
min_2 = 0
i-=1
if i != -1:
  max_1 = max(max(list_b[:-i-1]), max(list_a[:i + 1]))
  max_2 = max(max(list_b), max(list_a))
  
  min_2 = abs(max_1 + max_2)
  
  #print(min_1)
else:
  min_2 = list_a[-1] + list_b[-1]

print(min(min_1, min_2))