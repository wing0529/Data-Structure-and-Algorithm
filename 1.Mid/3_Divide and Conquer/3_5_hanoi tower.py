
'''
하노이 탑 
Step 1: move n-1 from source → extra   (using dst)
Step 2: move 1 (largest) from source → dst
Step 3: move n-1 from extra → dst     (using source)

'''

def hanoi(disks, source, dst, extra):
    if disks == 1:
        hanoi.count += 1
        print(f'{hanoi.count}: move from {source} to {dst}')
    else:
        # 1단계: source → extra (목표는 extra, dst는 중간 경유지)
        hanoi(disks - 1, source, extra, dst)

        # 2단계: 가장 큰 원판 source → dst
        hanoi.count += 1
        print(f'{hanoi.count}: move from {source} to {dst}')

        # 3단계: extra → dst (목표는 dst, source가 중간 역할)
        hanoi(disks - 1, extra, dst, source)


hanoi.count=0
hanoi(3,1,3,2)
