n = int(input())
triangle = [ list(map(int, input().split())) for _ in range(n)]


for i in range(1,n):
    for j in range(len(triangle[i])):

        if j == 0:
            left_up, right_up = 0, triangle[i-1][j]
        elif j == i:
            left_up, right_up = triangle[i-1][j-1], 0
        else:
            left_up, right_up = triangle[i-1][j-1], triangle[i-1][j]

        triangle[i][j] += max(left_up, right_up)

print(max(triangle[n-1]))

        
        