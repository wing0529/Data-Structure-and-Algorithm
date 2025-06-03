def hanoi(disks, src, dst, extra):
    if disks == 1:
        # base case: 원판 1개 → 바로 src → dst
        hanoi.count += 1
        hanoi.moves.append((src, dst))
    else:
        # Step 1: n-1개를 src → extra (보조 dst)
        hanoi(disks - 1, src, extra, dst)

        # Step 2: 큰 원판 1개를 src → dst
        hanoi.count += 1
        hanoi.moves.append((src, dst))

        # Step 3: n-1개를 extra → dst (보조 src)
        hanoi(disks - 1, extra, dst, src)

# 초기화
hanoi.count = 0
hanoi.moves = []

def printing(disks, src, dst, extra):
    hanoi(disks, src, dst, extra)
    print(hanoi.count)
    for i in range(hanoi.count):
        print(*hanoi.moves[i])

# 입력 및 실행
n = int(input())
printing(n, 1, 3, 2)
