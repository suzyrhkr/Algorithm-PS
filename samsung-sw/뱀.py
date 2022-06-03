import sys

input = sys.stdin.readline
n = int(input())
k = int(input())

space = [[0] * n for _ in range(n)]
snake_pos = [(0,0)]
space[0][0] = 'x'
direction = 1

for _ in range(k):
    row, col = map(int, input().split())
    space[row - 1][col - 1] = 1

l_info = []
l = int(input())
for _ in range(l):
    x, d = list(input().split())
    l_info.append((int(x), d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn(direction, d):
    if d == 'L':
        direction = (direction - 1) % 4
    elif d == 'D':
        direction = (direction + 1) % 4
    return direction

t = 0
index = 0
flag = False

while True:
    x = l_info[index][0]

    while True:
        head_x, head_y = snake_pos[-1][0], snake_pos[-1][1]
        nx, ny = head_x + dx[direction], head_y + dy[direction]
        # 칸의 범위를 벗어난 경우 or 자신의 몸에 부딪힌 경우
        if (0 <= nx < n and 0 <= ny < n) and space[nx][ny] != 'x':
            # 다음 칸에 사과가 있는 경우
            if space[nx][ny] == 1:
                space[nx][ny] = 'x'  # 사과 없어짐
                snake_pos.append((nx, ny))

            # 사과가 없는 경우
            elif space[nx][ny] == 0:
                tail_x, tail_y = snake_pos.pop(0)
                space[tail_x][tail_y] = 0  # 초기화
                space[nx][ny] = 'x'
                snake_pos.append((nx, ny))
        else:
            t += 1
            flag = True
            break
        t += 1

        if index < len(l_info) and t == l_info[index][0]:
            direction = turn(direction, l_info[index][1])
            index += 1
    if flag:
        break

print(t)

