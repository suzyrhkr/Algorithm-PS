n = 5
space = [[(i*n)+j for j in range(n)] for i in range(n)]

# clockwise 90°
def clockwise_rotate():
    rotated_space = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_space[j][n - i - 1] = space[i][j]
    return rotated_space

for row in space:
    print(row)
print()

ret = clockwise_rotate()
for row in ret:
    print(row)

'''
space:
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]

rotated_space:
[20, 15, 10, 5, 0]
[21, 16, 11, 6, 1]
[22, 17, 12, 7, 2]
[23, 18, 13, 8, 3]
[24, 19, 14, 9, 4]
'''

n = 5
space = [[(i*n)+j for j in range(n)] for i in range(n)]

# counterclockwise 90°
def counterclockwise_rotate():
    rotated_space = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
             rotated_space[n - j - 1][i] = space[i][j]
    return rotated_space

for row in space:
    print(row)
print()

ret = counterclockwise_rotate()
for row in ret:
    print(row)

'''
space:
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[10, 11, 12, 13, 14]
[15, 16, 17, 18, 19]
[20, 21, 22, 23, 24]

rotated_space:
[4, 9, 14, 19, 24]
[3, 8, 13, 18, 23]
[2, 7, 12, 17, 22]
[1, 6, 11, 16, 21]
[0, 5, 10, 15, 20]
'''