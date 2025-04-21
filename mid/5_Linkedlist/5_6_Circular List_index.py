
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

