class Solution(object):
    def matrixScore(self, grid):
        answer = 0
        matrix = []
        
        for row in grid:
            mask = 2**len(row)-1
            row_num = int("".join([str(x) for x in row]),2)
            row_num = max(row_num, row_num^mask)
            matrix.append(bin(row_num)[2:])
       
        for i, col in enumerate(range(len(matrix[0]))):
            cnt_one = 0
            for row in range(len(matrix)):
                if matrix[row][col]=='1':
                    cnt_one+=1
           
            exp = max(cnt_one, len(matrix)-cnt_one)
            answer += exp*pow(2,len(matrix[0])-i-1)
            
        return answer
        
        
        
        
        
                
            
            