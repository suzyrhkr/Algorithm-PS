n, m = map(int, input().split())
x, y, direction = map(int, input().split())

map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = [[0 for i in range(m)] for j in range(n)]
check[x][y] = 1 

turn_count = 0
count = 1

while True:
    direction -= 1
    if direction < 0:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if map_list[nx][ny] == 0 and check[nx][ny] == 0:
        check[nx][ny] = 1
        x = nx
        y = ny
        turn_count = 0
        count += 1
        continue

    else:
        turn_count += 1
   
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
 
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
     
        else:
            break
        turn_count = 0

print(count)