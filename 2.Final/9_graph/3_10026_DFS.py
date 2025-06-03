import sys
import copy

def depth_first_search(graph, row, col):
    """
    스택을 이용한 비재귀 DFS 함수
    graph: 2차원 리스트 (색상 정보 혹은 'X' 처리된 상태)
    row, col: DFS 시작 좌표
    """
    stack = [(row, col)]                   # 스택에 시작 좌표를 넣는다
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌, 우, 상, 하 이동 방향

    color = graph[row][col]                # 현재 영역의 색을 저장
    graph[row][col] = 'X'                  # 시작 좌표를 방문 표시('X'로 덮음)

    while stack:
        row, col = stack.pop()                 # 스택에서 하나를 꺼냄
        for m in range(4):# 이동할 좌표가 유효한지, 같은 색인지, 방문되지 않았는지 확인
            next_row, next_col = row,col
            next_row += move[m][0]
            next_col += move[m][1]
            if not check_move(graph, next_row, next_col, color):
                continue
            stack.append((next_row, next_col))         # 조건이 충족되면 스택에 추가
            graph[next_row][next_col] = 'X'            # 방문 표시

def check_move(graph, row, col, color):
    """
    DFS 혹은 BFS 전용으로, 다음 좌표로 이동 가능한지 검사
    graph: 2차원 리스트
    row, col: 검사할 좌표
    color: 기준 색 (시작 좌표의 색)
    반환값: True(이동 가능), False(이동 불가)
    """
    # 1) 범위를 벗어나는지 확인
    if row < 0 or row >= size:
        return False
    if col < 0 or col >= size:
        return False
    # 2) 색상이 기준 색(color)과 일치하는지 확인
    if graph[row][col] != color:
        return False
    # 3) 이미 방문('X'로 표시)된 곳인지 확인
    if graph[row][col] == 'X':
        return False
    return True


#  txt 받은거 graph로 2차원배열 저장
sys.stdin = open('C:\\Narae\\kw\\2025\\25-1\\class\\DSA\\Data-Structure-and-Algorithm\\Final\\9_graph\\A10026.txt', 'r')
input = sys.stdin.readline
size = int(input()) # 정사각형 한 변의 길이 N
_original = [list(input().strip()) for _ in range(size)]  # 원본 색상 맵을 2차원 리스트로 읽어들임


graph_normal = copy.deepcopy(_original)  # graph_normal deep copy
count_normal = 0
for i in range(size):
    for j in range(size):
        # 아직 방문하지 않은 칸('X'가 아닌 경우)이면 새로운 영역 시작
        if graph_normal[i][j] != 'X':
            depth_first_search(graph_normal, i, j)
            count_normal += 1              # 연결된 영역 하나를 찾았으므로 카운트 증가

# graph deep copy -> 적록색약 서치 (DFS)
graph_colorblind = copy.deepcopy(_original)  
for i in range(size):
    for j in range(size):
        # 'G'를 모두 'R'로 바꿔 적록색약 시야를 구현
        if graph_colorblind[i][j] == 'G':
            graph_colorblind[i][j] = 'R'

count_colorblind = 0
for i in range(size):
    for j in range(size):
        if graph_colorblind[i][j] != 'X':
            depth_first_search(graph_colorblind, i, j)
            count_colorblind += 1

# DFS 버전 결과 출력: 정상인 시야의 영역 수, 적록색약 시야의 영역 수
print(count_normal, count_colorblind)
