
fruits = ['orange','apple','banana']
print(len(fruits)) # 3

fruits.append('kiwi')
print(fruits) #['orange','apple','banana','kiwi']

fruits.insert(2,'pear')
print(fruits) # ['orange','apple','pear','banana','kiwi']

fruits.pop(1) #'apple' -> index 끄집어내기 !!
print(fruits) #['orange','pear','banana','kiwi']

fruits.pop() #마지막 index 끄집어 내기 'kiwi'
print(fruits)#['orange','pear','banana']

fruits.remove('banana')
print(fruits) #['orange','pear']

fruits = ['orange','apple','pear','banana','kiwi']
index = 3
fruits[index] # 'banana'

index += 2 #index = 5
fruits[index] # error, list index out of range

index = 3
index +=2 
if index >= len(fruits): #5 > 5
    index = index % len(fruits) # index -> 0

fruits[index] # 'orange'

