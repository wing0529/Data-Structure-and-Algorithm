from Circularlist import CircularSLL

words = CircularSLL()
words.insert(None, 'EGG')                     # head = EGG
words.insert(words.head, 'HAM')               # EGG → HAM
words.insert(words.head.next, 'SPAM')         # EGG → HAM → SPAM
words.insert(words.head, 'FISH')              # EGG → FISH → HAM → SPAM
for word in words.traverse():
    print(word)


words.remove(words.head) #head 다음 노드 삭제 : EGG → HAM → SPAM
words.remove(words.head.next)#HEAD 다음 다음 노드 삭제 = SPAM 삭제 : EGG HAM
for word in words.traverse():
    print(word)
