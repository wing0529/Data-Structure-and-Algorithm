def partitions(data,p,r):
    pivot = data[r]

    i = p-1
    for j in range(p,r):
        if data[j]<=pivot:
            i+=1
            data[i],data[j]=data[j],data[i]

    data[i+1], data[r] = data[r], data[i+1]
    return i+1

def quick_sort(data,p,r):
    if p<r:
        pivot_index = partitions(data,p,r)
        quick_sort(data,p,pivot_index-1)
        quick_sort(data,pivot_index+1,r)

test = [2,8,7,1,3,5,6,4]
quick_sort(test,0,len(test)-1)
print(test)
print(*test)
