
'''

# linked list로 queue 만들기 

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0

    def enqueue(self,data):
        node = Node(data)

        if self.size ==0:
            self.head = node
            self.tail = node
        else:
            self.tail.next=node
            self.tail=node
        self.size +=1

    def dequeue(self):
        if self.size ==0:
            return None
        self.size -=1

        data = self.head.data
        self.head = self.head.next
        return data
    
    def get_size(self):
        return self.size
    
    def front(self):# return top card value
        return self.head.data if self.head else None
        # if self.head -> return self.head.data
        # else -> return None

def card2(n):
    q = Queue()
    for i in range(1,n+1):
        q.enqueue(i)

    while q.get_size()>1:
        q.dequeue() # delete top card
        a = q.dequeue()
        q.enqueue(a)

    return q.front()

n = int(input("카드 개수를 입력 : "))
print(card2(n))
'''


# Deque로 queue 만들기 1

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0] if self.queue else None


def card2(n):
    
    q = Queue()

    for i in range(1,n+1):
        q.enqueue(i)

    while q.size() > 1:
        q.dequeue()
        a = q.dequeue()
        q.enqueue(a)

    return q.front()
    
n = int(input("카드 개수를 입력 : "))
print(card2(n))


# Deque로 queue 만들기 2

from collections import deque

def card2(n):
    q = deque(range(1,n+1))

    while len(q)>1:
        q.popleft()
        q.append(q.popleft())

    return q[0]

n = int(input("카드 개수를 입력 : "))
print(card2(n))