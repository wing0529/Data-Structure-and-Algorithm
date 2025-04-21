
def bubble_sort(unordered):
    n = len(unordered)
    for i in range(1, n):  # i = 1 to n-1
        for j in range(n - 1, i - 1, -1):  # j = n-1 down to i
            if unordered[j] < unordered[j - 1]:
                unordered[j], unordered[j - 1] = unordered[j - 1], unordered[j]


# 테스트
test = list('SORTINGEXAMPLE')
bubble_sort(test)
print(*test,sep=', ')
