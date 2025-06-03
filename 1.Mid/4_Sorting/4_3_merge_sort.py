def merge(data,p,q,r):
    left = data[p:q+1]
    right = data[q+1:r+1]
    left.append(float('inf'))
    right.append(float('inf'))
    
    i=j=0
    for k in range(p,r+1):
        if left[i]<=right[j]:# 같음이 여기들어있음으로, 둘이 동일한 값이면 왼쪽꺼 먼저 !! 
            data[k]=left[i]
            i+=1
        else:
            data[k]=right[j]
            j+=1

def merge_sort(data,p,r):
    if p<r:
        q = (p+r)//2
        merge_sort(data,p,q)
        merge_sort(data,q+1,r)
        merge(data,p,q,r)

test = [8,3,2,9,7,1,5,4]
merge_sort(test,0,len(test)-1)
print(test)
print(*test)