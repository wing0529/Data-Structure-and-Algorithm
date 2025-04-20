#list에 담긴 data중 가장 큰 것을 찾는 find max 함수

def recursive_find_max(data,left,right):
    if left == right:
        return data[left]
    mid = (left+right)//2
    x = recursive_find_max(data,left,mid)
    y = recursive_find_max(data,mid+1,right)

    if x > y:
        return x
    else:
        return y
    # x if x>y else y로 1줄로 줄여서도 가능 ! 

a = list('TINYEXAMPLE')
print(recursive_find_max(a,0,len(a)-1))




## 1. Linear Search
def linear_find_max(data,left,right):
    max_val = data[left]
    for i in range(left+1,right+1):
        if data[i] > max_val:
            max_val = data[i]
    return max_val
a = list('TINYEXAMPLE')
print(linear_find_max(a,0,len(a)-1))

# 2. Iterative Find Max
def iterative_find_max(data,left,right):
    max = data[left]
    for i in range(left+1,right+1):
        if data[i]>max:
            max = data[i]
    return max
a = list('TINYEXAMPLE')
print(iterative_find_max(a,0,len(a)-1))

# Binary Search (unsorted list) # 반복분 + 바이너리 형식이라 O(n)임 !! 
def binary_find_max(data, left, right):
    max_val = data[left]
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 기준 좌우값과 비교
        if data[mid] > max_val:
            max_val = data[mid]
        if data[left] > max_val:
            max_val = data[left]
        if data[right] > max_val:
            max_val = data[right]
        
        # 범위 줄이기 (양쪽 한 칸씩 좁힘 — binary 구조처럼)
        left += 1
        right -= 1

    return max_val
a = list('TINYEXAMPLE')
print(binary_find_max(a,0,len(a)-1))


a = list('TINYEXAMPLE')
print(len(a)-1)
print(recursive_find_max(a,0,len(a)-1))
print(linear_find_max(a,0,len(a)-1))
print(iterative_find_max(a,0,len(a)-1))
print(binary_find_max(a,0,len(a)-1))