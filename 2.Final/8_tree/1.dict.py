## python dictionary

### dict 는 중괄호
a = {}

### dict 만드는 법 (1) 중괄호
a = { 1 : 'mustang', 2:'genesis','brand':'Ford'}
print(a)
print(type(a))

### dict 만드는 법 (2) dict 함수 이용 
a = dict([('brand','Ford'),('model','taurus')])
print(a)
print(type(a))


a = {'name':'Jack', 'age':26}

### dict read (1) 참조 
a['name']
a['address'] # key를 가진 value가 없을때 ! 에러 발생

### dict read (2)  get 함수 이용 
a.get('name')
a.get('address') # key를 가진 value가 없을때도 오류 발생 x

print(a['age'])
a['age'] = 27
print(a['age'])
a['new']='250528'
print(a['new'])

print(a)
a.pop('name')
print(a)

a.clear()
print(a)