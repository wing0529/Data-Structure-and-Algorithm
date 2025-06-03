n = int(input())  # 테스트 케이스 수

for _ in range(n):
    s = []               # 스택
    data = input()       # 괄호 문자열
    eflag = True         # 올바른 괄호인지 판별하는 플래그

    for c in data:
        if c == '(':     # 여는 괄호는 push
            s.append(c)
        else:            # 닫는 괄호일 경우
            if len(s) == 0:  # 스택이 비었으면 오류
                eflag = False
                break
            else:
                s.pop()  # 올바른 짝이므로 pop

    # 스택이 비었고 중간에 오류 없었으면 YES
    if len(s) == 0 and eflag:
        print('YES')
    else:
        print('NO')
