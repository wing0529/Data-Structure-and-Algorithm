### set도 중괄호, dict와 기호과 동일 ! , 초기화를 어떤 문법으로 하는지에 따라 set인지 dict인지 결정된다.
a = {} # dict으로 자동으로 만들어짐, 만약 비어있는 set을 만들고자한다면 set()사용 ! 
a = set()

a={'a':1}
print(type(a))
a={1,2,3}
print(type(a))

# 집합과 동일한 개념으로, 다양한 자료형을 담을 수 있다 
a = { 1.0,"hello",(1,2,3)}

# 중복을 허용하지 않음. unique한 값만
a = {1,2,3,4,3,2}
a

# (2) set함수 사용, 이것도  unique한 값만 ! 
a = set([1,2,3,2])
a

a = set()

a.add(2)
print(a)

a.update([3,4]) #여러개 동시에 추가
print(a)

# remove
a.discard(3)

print(a)

a.update([3,4]) #여러개 동시에 추가
print(a)

#set object안에 없어도 아무 이유없이 진행가능
a.discard(5)

#set object안에 없으면 에러발생
a.remove(5) 


#집합연산기호를 set에서 활용할수있음

a = {1,2,3,4,5}
b = {4,5,6,7,8}


print(a|b)
print(a&b)

print(a-b)

