n = 5
space =[[0]*n for _ in range(n)]
# 방향: 왼쪽 아래쪽 오른쪽 위쪽
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def init_grid():
    x, y = n//2, n//2
    direction, move_cnt, num, dist = 0, 0, 0, 1

    while True:
        move_cnt += 1
        for _ in range(dist):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if [nx, ny] == [0, -1]:
                return
            
            num += 1
            space[nx][ny] = num
            x, y = nx, ny
        
        if move_cnt == 2:
            dist += 1
            move_cnt = 0
        direction = (direction + 1) % 4

init_grid()

for row in space:
    print(row)
            
'''
[24, 23, 22, 21, 20]
[9, 8, 7, 6, 19]
[10, 1, 0, 5, 18]
[11, 2, 3, 4, 17]
[12, 13, 14, 15, 16]
'''