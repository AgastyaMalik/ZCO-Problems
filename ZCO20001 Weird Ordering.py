t = int(input())
def order(arr, i):
    if len(arr) <= 1 :
      return arr

    l = []  
    r = []
    n = len(arr) - 1
    for j in range(n):
       if ( (arr[j]%(2**(i+1)))  < 2**i):
          l.append(arr[j])
       else:
          r.append(arr[j])
    

    l = order(l, i + 1)
    r = order(r, i + 1)
    c = l+r
    return c

for i in range(t):
    arr =[]
    p,idx = map(int,input().split())
    for i in range(2**p -1):
        arr.append(i)
    print(order(arr,0))