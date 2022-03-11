def solution(line):
    star = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i][0], line[i][1], line[i][2]
            c, d, f = line[j][0], line[j][1], line[j][2]
            
            if a*d-b*c != 0:
                x, y = (b*f-e*d)/(a*d-b*c), (e*c-a*f)/(a*d-b*c)
                if x == int(x) and y == int(y):
                    star.append([int(x),int(y)])
    
    x_min, x_max, y_min, y_max = min(star)[0],max(star)[0],min(star,key = lambda x: x[1])[1],max(star,key = lambda x: x[1])[1]
    answer = [["."]*(x_max-x_min+1) for _ in range(y_max-y_min+1)]

    for s in star:
        a, b = s
        x,y = abs(y_max-b) , abs(x_min-a)
        answer[x][y] = '*'
    
    for i,v in enumerate(answer):
        answer[i] = ''.join(v)
    
    return answer