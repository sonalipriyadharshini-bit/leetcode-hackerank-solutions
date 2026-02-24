from itertools import product
K,M = map(int,input().split())   
lists=[]
for i in range (K):
    data = list(map(int,input().split()))
    Ni = data[0]
    elements = data[1:]
    lists.append(elements)
max_value = 0
for combination in product(*lists):
    total = 0
    for x in combination:
        total +=x *x
    total %= M 
    max_value = max(max_value,total)
print(max_value)
