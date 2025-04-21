from Circularlist import CircularSLL

words = CircularSLL()
words.insert(None, 'EGG')                     # 첫 노드 삽입 (EGG)
words.insert(words.head, 'HAM')               # EGG 뒤에 HAM 삽입 : EGG HAM
words.insert(words.head.next, 'SPAM')         # HAM 뒤에 SPAM 삽입 : EGG HAM SPAM
words.insert(words.head, 'FISH')              # EGG 뒤에 FISH 삽입 : EGG FISH HAM SPAM

for word in words.traverse():
    print(word)
# 순회 출력: EGG → FISH → HAM → SPAM

words.remove(words.head)                      # EGG 제거 → head = FISH, 전체 : FISH HAM SPAM
words.remove(words.head.next)                 # HAM 제거 -> head = FISH, 전체 : FISH SPAM
words.remove(words.head)                      # FISH 제거 → head = SPAM, 전체 : SPAM
