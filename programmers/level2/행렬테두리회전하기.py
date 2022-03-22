# time limit 63.6/100
import copy
def solution(rows, columns, queries):
    answer, space = [], []
    num = 1
    for i in range(rows):
        space.append(list(range(num,num+columns)))
        num += columns

    for q in queries:
        space_copy = copy.deepcopy(space)
        start_x, start_y, end_x, end_y = q
        tmp = []

        for i in range(start_x-1, end_x):
            for j in range(start_y-1, end_y):      
                if j == start_y-1 and i!= end_x-1: 
                    tmp.append(space[i][j])
                    space[i][j] = space_copy[i+1][j]
                if i == start_x-1 and j!= start_y-1:
                    tmp.append(space[i][j])
                    space[i][j] = space_copy[i][j-1]
                if j == end_y-1 and i!=start_x-1:
                    tmp.append(space[i][j])
                    space[i][j] = space_copy[i-1][j]
                if i == end_x-1 and j!=end_y-1:
                    tmp.append(space[i][j])
                    space[i][j] = space_copy[i][j+1]      

        answer.append(min(tmp))
        
    return answer
                
#---other solution---
def solution(rows, columns, queries):
    answer, space = [], []
    num = 1
    for i in range(rows):
        space.append(list(range(num,num+columns)))
        num += columns

    for q in queries:
        start_x, start_y, end_x, end_y = q
        tmp = space[start_x-1][start_y-1]
        min_value = tmp
        
        for i in range(start_x, end_x):
            space[i-1][start_y-1] = space[i][start_y-1]
            min_value = min(min_value, space[i][start_y-1])
        for j in range(start_y, end_y):
            space[end_x-1][j-1] = space[end_x-1][j]
            min_value = min(min_value, space[end_x-1][j])
        for i in range(end_x-1, start_x-1, -1):
            space[i][end_y-1] = space[i-1][end_y-1]
            min_value = min(min_value, space[i-1][end_y-1])
        for j in range(end_y-1, start_y-1, -1):
            space[start_x-1][j] = space[start_x-1][j-1]
            min_value = min(min_value, space[start_x-1][j-1])

        space[start_x-1][start_y] = tmp

        answer.append(min_value)
        
    return answer
                

