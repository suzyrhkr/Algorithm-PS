# 2' 45
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
info = list(map(int, input().split()))

space = []
for i in range(n):
    space.append([info[i]])

def add_fish():
    min_value = min(space)[0]
    for i, num_fish in enumerate(space):
        if num_fish[0] == min_value:
            space[i][0] += 1

def stack_space():
    fish = space.pop(0)
    space[0].extend(fish)

def go_up():
    while True:
        w = 0
        for i in range(len(space)):
            if 2 <= len(space[i]):
                w += 1
        h = len(space[0])

        if len(space) - w < h: # exit condition
            break

        rotate_list = [[] for _ in range(h)]
        for i in range(w):
            for j in range(h):
                rotate_list[j].append(space[i][j])
        for _ in range(w):
            space.pop(0)
        for i in range(h):
            reversed_list = rotate_list[i]
            reversed_list.reverse()
            space[i].extend(reversed_list)

def second_go_up():
    for _ in range(2):
        length = len(space) // 2
        rotate_list = [[] for _ in range(length)]
        w, h = length, len(space[0]) # 4 2
        for i in range(w):
            for j in range(h):
                rotate_list[i].append(space[i][j])
        for _ in range(w):
            space.pop(0)

        reversed_list = [[] for _ in range(w)]

        for i in range(w):
            rotate_180 = rotate_list[i]
            rotate_180.reverse()
            reversed_list[w-i-1].extend(rotate_180)

        for i in range(w):
            space[i].extend(reversed_list[i])

def move_fish():
    diff = [[0]*len(row) for row in space]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(len(space)):
        for j in range(len(space[i])):
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                if 0 <= nx and nx < len(space) and 0 <= ny and ny < len(space[i]):
                    if ny <= len(space[nx]) - 1: # 접근하지 못하는 칸 처리
                        if space[nx][ny] < space[i][j]:
                            d = (space[i][j] - space[nx][ny]) // 5
                            if 0 < d:
                                diff[i][j] -= d
                                diff[nx][ny] += d

    for i in range(len(space)):
        for j in range(len(space[i])):
            space[i][j] += diff[i][j]

def move_fish2():
    diff = [[0]*len(row) for row in space]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(len(space)):
        for j in range(len(space[i])):
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                if 0 <= nx and nx < len(space) and 0 <= ny and ny < len(space[i]):
                    if space[nx][ny] < space[i][j]:
                        d = (space[i][j] - space[nx][ny]) // 5
                        if 0 < d:
                            diff[i][j] -= d
                            diff[nx][ny] += d

    for i in range(len(space)):
        for j in range(len(space[i])):
            space[i][j] += diff[i][j]

def one_line(sp):
    new_space = []
    for i in range(len(sp)):
        for j in range(len(sp[i])):
            new_space.append([sp[i][j]])
    return new_space

cnt = 0
while True:
    if max(space)[0] - min(space)[0] <= k:
        break
    # 1. 물고기 수가 가장 적은 어항에 물고기 한 마리 넣음 (여러 개: 물고기 수 최소인 어항에 모두 한 마리씩 넣음)
    add_fish()
    # 2. 어항 쌓기 -> 가장 왼쪽 어항을 오른쪽 어항 위에 쌓기
    stack_space()
    # 3. 공중 부양 -> 2개 이상 쌓인 어항을 공중 부양, 전체를 시계방향 90도 회전
    go_up()
    # 4. 물고기 수 조절
    move_fish()
    # 5. 어항 다시 일렬로 놓기
    space = one_line(space)
    # 6.공중 부양 2
    second_go_up()
    # 7. 물고기 조절 작업 다시 시행.
    move_fish2()
    # 8. 일렬로 놓기.
    space = one_line(space)

    cnt += 1

print(cnt)

"""
어항 정리:
어항 n개, 각 어항에는 물고기가 한 마리 이상 있음
과정:
1. 물고기 수가 가장 적은 어항에 물고기 한 마리 넣음 (여러 개: 물고기 수 최소인 어항에 모두 한 마리씩 넣음)
2. 어항 쌓기 -> 가장 왼쪽 어항을 오른쪽 어항 위에 쌓기
3. 공중 부양 -> 2개 이상 쌓인 어항을 공중 부양, 전체를 시계방향 90도 회전
        -> 공중 부양 어항 중 가장 오른쪽에 있는 어항의 아래 바닥에 있는 어항이 있을 때까지 (종료 조건)
4. 물고기 수 조절: 인접한 칸에 대해 동시에 발생. 인접한 두 어항 물고기 수 차이 구함 이것을 5로 나눈 몫 d.
        0<d: 많은 곳 -> 적은 곳 d 마리 보내기
5. 어항 다시 일렬로 놓기: 왼쪽 -> 오른쪽, 아래 -> 위 방향으로
6. 공중 부양 2: 왼쪽 n/2 개 공중부양: 시계 방향 180도 회전하여 오른쪽 위에 놓기 -> 이것을 두 번 반복!!
        -> 두 번 반복 이후, 바닥에 있는 어항의 수 n/4개가 됨.
7. 물고기 조절 작업 다시 시행.
8. 일렬로 놓기.

output: 물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 어항을 몇 번 정리해야하는지 구해보자
"""