customers=int(input())
budget=[]
revenue =[]
for i in range(customers):
    x=int(input())
    budget.append(x)
budget.sort() 
for i in range(0,customers):
    revenue.append(budget[i]*(customers-i))
print(max(revenue))