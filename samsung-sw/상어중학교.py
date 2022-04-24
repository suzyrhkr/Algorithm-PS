# 1' 55 
import sys

input = sys.stdin.readline
n, m = map(int, input().split()) 
space = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1] # 오른쪽 아래 왼쪽 위
dy = [1, 0, -1, 0]

def dfs(x, y, visited, color, elements, rainbow):
    if not (0 <= x and x < n and 0 <= y and y < n):
        return elements, rainbow
    if visited[x][y]:
        return elements, rainbow
    if space[x][y] == -1:
        return elements, rainbow
    if (space[x][y] != 0 and space[x][y] != color):
        return elements, rainbow

    visited[x][y] = True
    elements.append([x,y])

    if space[x][y] == 0: # 무지개인 경우
        rainbow += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        _, rainbow = dfs(nx, ny, visited, color, elements, rainbow)
    return elements, rainbow

def gravity(table):
    # 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
    for i in range(n-1, -1, -1):
         for j in range(n-1, -1, -1):
             if space[i][j] == None:
                 continue
             if 0 <= space[i][j]:
                 curr_x, curr_y, elem = i, j, space[i][j]
                 while True:
                    nx, ny = curr_x + dx[1], curr_y + dy[1] # 다음 좌표
                    if not (0 <= nx and nx < n and 0 <= ny and ny < n):
                        break
                    if table[nx][ny] != None:
                        break
                    curr_x, curr_y = nx, ny

                 if (curr_x, curr_y) != (i, j):
                     table[curr_x][curr_y] = elem
                     table[i][j] = None
    return table

def rotate(table):
    new_table = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_table[n-j-1][i] = table[i][j]
    return new_table

#블록 그룹이 존재하는 동안 계속해서 반복
score = 0
while True:
    groups = {}
    group_info = []
    for i in range(n):
        for j in range(n):
            if space[i][j] == None:
                continue
            if 0 < space[i][j]: # 일반 블록인 경우에만.
                visited = [[False] * n for _ in range(n)]
                blocks, rainbow = dfs(i, j, visited, space[i][j], [], 0)
                if len(blocks) < 2: # 블록 개수 2 이상
                    continue
                blocks.sort(key=lambda x: (x[0], x[1]))
                for bx, by in blocks: # 블록 기준
                    if space[bx][by] != 0:
                        base_x, base_y = bx, by
                        break
                groups[(base_x, base_y)] = blocks
                group_info.append([len(blocks), rainbow, base_x, base_y])

    # 블록 그룹이 존재하는지 체크 -> Exit
    if not group_info:
        break

    set_group = []
    for group in group_info:
        if group not in set_group:
            set_group.append(group)

    # 크기가 큰 / 무지개 블록이 많은 / 기준 블록 행, 열이 가장 큰 것 [-크기, -무지개 블록 수, -i, -j]
    set_group.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    largest_group = set_group[0]

    # 블록 그룹이 제거되면 점수 획득
    for bx, by in groups[(largest_group[2], largest_group[3])]: # 딕셔너리에 들어있는 블록 좌표들
        space[bx][by] = None # 0으로 초기화

    score += largest_group[0]**2
    # 중력 작용
    space = gravity(space)
    # 90도 반시계 방향 회전
    space = rotate(space)
    # 다시 중력 작용
    space = gravity(space)

print(score)
