words = []

words.append('eggs')
words.append('spam')
words.append('ham')

# len(words) = 3

index = 0 
while len(words)>0:
    index +=2 # index = 2 , 4, 2
    if index >= len(words): 
        index %= len(words) # 4%2 = 0 (index), 2 % 1 -> 0 
    print(words.pop(index)) # 'ham', 'eggs' 'spam'
    if index == len(words): 
        index = 0
