class MaxHeap:
    def __init__(self,data_list=None):
        self.h = [0]
        if data_list is not None:
            self.h.extend(data_list)

        for i in range(self.size()//2,0,-1):
            self.max_heapify(i)

    def size(self):
        return len(self.h)-1

    def max_heapify(self,k):
        left = 2*k
        right = 2*k +1

        largest = k

        if left <=self.size() and self.h[left]>self.h[largest]:
            largest = left
        if right <=self.size() and self.h[right]>self.h[largest]:
            largest=right

        if k != largest:
            self.h[k], self.h[largest] = self.h[largest], self.h[k]
            self.max_heapify(largest)


    def heap_sort(self):
        save = self.h[:] # shallow copy
        sorted_list = self.h[1:]

        for i in range(self.size(),0,-1):
            self.h[1], self.h[i]=self.h[i],self.h[1]
            sorted_list[i-1] = self.h[i]
            self.h.pop()
            self.max_heapify(1)

        self.h=save
        return sorted_list



a = [4,8,7,2,9,10,5,1,3,6]
h1 = MaxHeap(a)
print(h1.h)

print(h1.heap_sort())
print(h1.h)