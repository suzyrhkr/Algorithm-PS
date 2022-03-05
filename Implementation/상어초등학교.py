# get input
n = int(input())
students_info = []
seats = [[0]*n for _ in range(n)]

for _ in range(pow(n,2)):
    line = list(map(int, input().split()))
    students_info.append((line[0], line[1:]))

# up, down, left, right
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# def
def findRowCol(seats, st, n):
    r,c = -1, -1
    for row in range(n):
        for col in range(n):
            if seats[row][col] == st:
                r, c = row, col 
    if r==c==-1:
        return False
    return r, c

def n_AdjacentEmptySeats(seats, r, c):
    cnt = 0
    empty_seats = []

    for x, y in zip(dx, dy):
        if  n <= r+x or r+x < 0 or n <= c+y or c+y < 0:
            continue
        if seats[r+x][c+y] == 0:
            empty_seats.append((r+x, c+y))
            cnt += 1
    return cnt, empty_seats

def n_favoriteStudents(seats, r, c, f_sts):
    cnt = 0

    for x, y in zip(dx, dy):
        if  n <= r+x or r+x < 0 or n <= c+y or c+y < 0:
            continue
        if seats[r+x][c+y] in f_sts:
            cnt += 1
    return cnt

def getScore(students_info, seats):
    score = 0
    
    for st, f_sts in students_info:
        cnt = 0
        r, c = findRowCol(seats, st, n)
        for x, y in zip(dx, dy):
            if  n <= r+x or r+x < 0 or n <= c+y or c+y < 0:
                continue
            if seats[r+x][c+y] in f_sts:
                cnt += 1
        if 0<cnt:
            score += 10**(cnt-1)
    return score

# main code
for st, f_sts in students_info:
    tmp_seats = []
    if st == students_info[0][0]:
        seats[1][1] = st
        continue

    # condition 1
    first_tmp = {}
    for i in range(n):
        for j in range(n):
            if seats[i][j] != 0:
                continue
            cnt = n_favoriteStudents(seats, i, j, f_sts)
            first_tmp[(i, j)] = cnt
    tmp = [k for k,v in first_tmp.items() if max(first_tmp.values()) == v]

    if len(tmp) == 1:
        s_x, s_y = tmp[0][0], tmp[0][1]
        seats[s_x][s_y] = st
        continue

    # condition 2
    second_tmp = {}
    for row, col in tmp:
        cnt, _ = n_AdjacentEmptySeats(seats, row, col)
        second_tmp[(row, col)] = cnt
    tmp = [k for k,v in second_tmp.items() if max(second_tmp.values()) == v]

    if len(tmp) == 1:
        s_x, s_y = tmp[0][0], tmp[0][1]
        seats[s_x][s_y] = st
        continue

    # condition 3
    tmp.sort(key=lambda x: (x[0],x[1]))
    s_x, s_y = tmp[0]
    seats[s_x][s_y] = st
    
score = getScore(students_info, seats)
print(score)