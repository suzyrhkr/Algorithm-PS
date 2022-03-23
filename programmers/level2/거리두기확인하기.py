# 41분 20초

def search(place, i, j):
    delta = [(-1,-1),(-1,0),(-1,1),(0,1),
             (1,1),(1,0),(1,-1),(0,-1),
             (-2,0),(0,2),(2,0),(0,-2)]
    ret = True
    
    for dx, dy in delta:
        nx, ny = i+dx, j+dy
        if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
            if place[nx][ny] == 'P': # p가 있는 경우 -> 파티션 검사
                # case 1: (맨해튼 거리 1)
                if abs(i-nx) + abs(j-ny) == 1:
                    ret = False
                # case 2: 일렬 (맨해튼 거리 2)
                if i == nx or j == ny: # 일렬인 경우
                    x, y = (i+nx)//2, (j+ny)//2
                    if place [x][y] != 'X':
                        ret = False
                # case 3: 대각선 (맨해튼 거리 2)
                else:
                    if not (place[i][ny] == 'X' and place[nx][j] == 'X'):
                        ret = False
    return ret
    
def solution(places):
    answer = []
    
    for place in places:
        flag = True
        for i, row in enumerate(place):
            for j, node in enumerate(row):
                if node == 'P': 
                    ret = search(place, i, j)
                    if ret == False:
                        flag = False
        
        answer.append(1) if flag == True else answer.append(0)

    return answer
