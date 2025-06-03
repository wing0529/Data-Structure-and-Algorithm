
def insertion_sort(data):
    for j in range(1,len(data)):
        key = data[j]
        i = j-1
        while i>=0 and data[i] > key:
            data[i+1] = data[i]
            i -= 1
        data[i+1] = key

test =[5,2,4,6,1,3]
insertion_sort(test)
print(test)