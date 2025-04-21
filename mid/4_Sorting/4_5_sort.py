numbers = [3, 8, 5, 1]
numbers.sort()
print(numbers)
# 오름차순 정렬 → [1, 3, 5, 8]

numbers.sort(reverse=True)
print(numbers)
# 내림차순 정렬 → [8, 5, 3, 1]
# reverse=True는 True/1/100 다 가능. False/0만 아니면 동작함

tuples = [(2,2), (3,4), (4,1), (1,3)]
tuples.sort()
print(tuples)
# 튜플 전체 기준 오름차순 정렬 (x[0] → x[1])
# 동일한 첫 번째 값이 있을 경우, 두 번째 값도 오름차순으로 비교됨
# 파이썬 정렬은 stable이라 결과 같아 보이지만, 이 자체는 unstable 정렬 방식

tuples.sort(key=lambda x: x[1])
print(tuples)
# 두 번째 값(x[1]) 기준 오름차순 정렬
# 같은 x[1]일 경우 기존 순서 유지 → stable 정렬

test = [(2,'b'), (3,'d'), (3,'a'), (1,'c')]
test.sort()
print(test)
# 튜플 전체 기준 정렬 → x[0], x[1] 순으로 비교
# (3,'a')와 (3,'d')처럼 x[0]이 같은 경우 x[1]도 비교됨 → unstable

test = [(2,'b'), (3,'d'), (3,'a'), (1,'c')]
test.sort(key=lambda x: x[0])
print(test)
# x[0] 기준 오름차순 정렬
# 같은 x[0]이면 기존 순서 유지 → stable

test = [(2,'b'), (3,'d'), (3,'a'), (1,'c')]
test.sort(reverse=True)
print(test)
# 전체 튜플 기준 내림차순
# x[0] 기준으로 내림차순, 같으면 x[1]도 비교 → unstable

test = [(2,'b'), (3,'d'), (3,'a'), (1,'c')]
test.sort(key=lambda x: (-x[0], x[1]))
print(test)
# x[0] 내림차순, 같은 경우 x[1] 오름차순
# 복합 키 정렬 (다중 기준), stable이지만 정렬 기준이 x[1]로 바뀌므로 결과는 unstable처럼 보일 수 있음

test = [(2,'b'), (3,'d'), (3,'a'), (1,'c')]
test.sort(key=lambda x: x[1], reverse=True)
print(test)
# x[1] 기준 내림차순 정렬
# 같은 x[1]일 경우 기존 순서 유지 → stable

test.sort(key=lambda x: x[0])
print(test)
# x[0] 기준 오름차순 정렬, 동일한 값은 기존 순서 유지 → stable
