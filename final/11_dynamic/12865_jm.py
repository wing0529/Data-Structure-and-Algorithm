import sys

def knapsack(capacity,item):
    if capacity ==0 or item >=n:
        return 0
    if weight[item]>capacity:
        return knapsack(capacity,item+1)
    
    if _memo[(capacity,item)] is None:
        with_the_item = value[item] + knapsack(capacity-weight[item],item+1)
        without_the_item = knapsack(capacity,item+1)
        _memo[(capacity,item)]=max(with_the_item,without_the_item)
    return _memo[(capacity,item)]

#n,k = map(int,input().split())

sys.stdin=open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\Final\\11_dynamic\\12865.txt','r')
n, k = map(int, sys.stdin.readline().split())


_memo = {}
value = [0]*n
weight = [0]*n

for i in range(n):
    weight[i],value[i]=map(int,input().split())

for j in range(k+1):
    for l in range(n+1):
        _memo[(j,l)]=None

print(knapsack(k,0))