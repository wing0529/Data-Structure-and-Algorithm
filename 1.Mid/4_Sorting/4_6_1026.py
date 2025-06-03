'''
보물 문제

길이가 N인 정수 배열 A, B가 주어짐.
S = A[0]*B[0] + A[1]*B[1] + ... + A[N-1]*B[N-1]
S의 값을 최소로 만들기 위해 A는 재배열할 수 있지만, B는 그대로 유지됨.

아이디어: A의 가장 작은 수 * B의 가장 큰 수 → 최소 곱을 만들 수 있음
→ A는 오름차순 정렬
→ B는 내림차순 정렬한 복사본 사용 (원본 유지)
'''
# sort(), sorted() 사용한 보물 문제 

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()                         # A는 오름차순 정렬
B_sorted = sorted(B, reverse=True)  # B는 내림차순 복사 정렬

S = 0
for i in range(N):
    S += A[i] * B_sorted[i]      # 같은 인덱스끼리 곱해서 누적

print(S)


''' quick sort로 직접 정렬 구현한 보물 문제 '''

# PIVOT값을 뭐로 설정할 것인지에 따라 코드가 달라진다. 
#1. pivot = A[0]
def partition_pivot_first(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1

        if left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[first], arr[right] = arr[right], arr[first]
    return right

def quick_sort_pivot_first(arr, first, last):
    if first < last:
        pivot_index = partition_pivot_first(arr, first, last)
        quick_sort_pivot_first(arr, first, pivot_index - 1)
        quick_sort_pivot_first(arr, pivot_index + 1, last)


#2. pivot = A[-1]
def partition_pivot_last(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_pivot_last(arr, low, high):
    if low < high:
        pivot_index = partition_pivot_last(arr, low, high)
        quick_sort_pivot_last(arr, low, pivot_index - 1)
        quick_sort_pivot_last(arr, pivot_index + 1, high)

n = int(input())
A1 = list(map(int, input().split()))
A2 = A1[:]
B = list(map(int, input().split()))
B_sorted = sorted(B, reverse=True)

# 버전 1: 피벗 = A[0]
quick_sort_pivot_first(A1, 0, n - 1)
S1 = sum(a * b for a, b in zip(A1, B_sorted))

# 버전 2: 피벗 = A[-1]
quick_sort_pivot_last(A2, 0, n - 1)
S2 = sum(a * b for a, b in zip(A2, B_sorted))

print("pivot=A[0] 버전 결과:", S1)
print("pivot=A[-1] 버전 결과:", S2)
