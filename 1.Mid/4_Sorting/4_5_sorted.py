data = [3, 8, 5, 1]
data.sort()
print(data)
# 리스트 오름차순 정렬 (in-place, 원본 변경) → [1, 3, 5, 8]
# 파이썬의 sort()는 stable

data = [3, 8, 5, 1]
data1 = sorted(data)  # 새로운 리스트 생성 (원본 유지)
print(data1)  # [1, 3, 5, 8]
print(data)   # [3, 8, 5, 1]

data = (3, 8, 5, 1)
data1 = sorted(data)  # 튜플도 정렬 가능 → 결과는 리스트로 반환됨
print(data1)  # [1, 3, 5, 8] ← tuple 아님!
print(data)   # (3, 8, 5, 1) ← 원본 유지

data = {3, 8, 5, 1}  # 집합 (set)
data1 = sorted(data)  # 정렬된 리스트 반환
print(data1)  # [1, 3, 5, 8] ← set → list 변환됨
print(data)   # set은 순서 없는 자료형 → 출력 순서는 랜덤 (예: {8, 1, 3, 5})
