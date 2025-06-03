import heapq

def heapsort(iterable):
    print(iterable)
    h = []
    for value in iterable:
        heapq.heappush(h,value)
        print(h)
    return [heapq.heappop(h)for _ in range(len(h))]


a = [3,5,1,2,6,8,7]
heapq.heapify(a)
print(a)
print(heapsort(a))

b =[]
heapq.heappush(b,(5,'write code'))
heapq.heappush(b,(7,'write code'))
heapq.heappush(b,(1,'write code'))
print(heapq.heappop(b))