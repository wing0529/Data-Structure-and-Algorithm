
n , k = map(int,input().split())

jo = []

for i in range(1,n+1):
    jo.append(i) # 1,2,3,4,5,6,7

print('<', end='') # '< '

idx = 0  # 시작 인덱스

while jo:
    idx += k - 1  # k번 index 증가 시키기, 현재 위치를 포함하지 않아서 k-1칸 이동

    if idx >= len(jo):
        idx = idx % len(jo)  # 리스트 범위를 넘어가면 되돌림

    print(jo.pop(idx), end='')

    if jo:
        print(', ', end='')
    else:
        print('>')
