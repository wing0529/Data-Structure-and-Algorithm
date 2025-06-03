class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data): #리스트 맨 앞에 노드 추가
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):#전체 리스트 출력
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def merge_sort(self, head):# 재귀적으로 리스트를 반으로 나눈 뒤 정렬 -> 병합
        if head is None or head.next is None:
            return head  # base case

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # 분할

        # 재귀 정렬
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # 병합
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):#Slow-Fast 포인터로 중간 노드 반환
        if head is None:
            return head
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a, b):# 두 정렬된 리스트 병합
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def sort(self):#사용자용 정렬 메서드 (self.head 갱신 포함)
        self.head = self.merge_sort(self.head)

ll = LinkedList()
for value in [15, 10, 5, 20, 3, 2]:
    ll.push(value)

print("정렬 전", end=':') # 바로 출력
ll.print_list()
# 정렬 전:2 3 20 5 10 15 

ll.sort()

print("정렬 후:") # \n이 되서 출력된다.
ll.print_list()
'''
정렬 후:
2 3 5 10 15 20
'''
