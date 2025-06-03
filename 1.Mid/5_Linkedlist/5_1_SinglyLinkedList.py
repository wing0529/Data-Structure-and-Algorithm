from Linkedlist import SinglyLinkedList 
#Linkedlist.py안에 SinglyLinkedList 자료형 있음

words = SinglyLinkedList()

words.insert(None, 'eggs')              # head ← 'eggs'
words.insert(words.head, 'ham')         # 'eggs' 다음에 'ham'

for word in words.traverse():           # 출력: eggs → ham
    print(word)

words.remove(words.head)                # 'ham' 제거 (eggs → None)
words.remove(None)                      # 'eggs' 제거 (head = None)

