
fruits = ['orange','apple','pear','banana','kiwi']
index = 3
fruits.pop(index)#['orange','apple','pear','kiwi']
fruits[index]    #'banana'
fruits.pop(index)#['orange','apple','pear']
fruits[index]    #'kiwi'
fruits.pop(index) # error. 


fruits = ['orange','apple','pear','banana','kiwi']
fruits.pop(index)#'banana', ['orange','apple','pear','kiwi']
if index == len(fruits): #크기 동일 
    index = 0 #index 0으로
fruits[index] #'orange'

