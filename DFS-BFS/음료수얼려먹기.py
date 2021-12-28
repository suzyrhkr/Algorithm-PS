ice = [[0,0,1,1,0], [0,0,0,1,1],[1,1,1,1,1], [0,0,0,0,0]]
n, m = 4, 5
result = 0

def dfs(x, y):
    if x<0 or n<=x or y<0 or m<=y:
        return False

    if ice[x][y]==0:
        ice[x][y]=1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)
