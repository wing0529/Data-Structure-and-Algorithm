
from DoublyLinkedlist import DoublyLinkedlist
dll = DoublyLinkedlist()
dll.insert(None, 1)# 처음에는 무조건 none
dll.insert(dll.head, 4) # 1 다음에 삽입
dll.insert(dll.head.next, 16) # 4 다음에 삽입
dll.insert(None, 9) # 맨 앞에 삽입
dll.insert(None, 25) # 맨 앞에 삽입 

print("정방향 (head → tail):")
print(*list(dll.traverse_forward()))   
#25 9 1 4 16

print("역방향 (tail → head):")
print(*list(dll.traverse_backward())) 
#16 4 1 9 25

dll.delete(dll.head)
print(list(dll.traverse_forward()))   
# [9, 1, 4, 16]

# dll.delete(None) <- 오류 발생 ! 
  
dll.delete(dll.head.next)
print(list(dll.traverse_forward()))   
# [9, 4, 16]