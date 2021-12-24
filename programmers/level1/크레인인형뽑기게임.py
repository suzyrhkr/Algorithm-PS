def solution(board, moves):
    answer = 0
    bascket = []

    for move in moves:
        i=0
        while board[i][move-1]==0 and i<len(board)-1:
            i+=1
        
        if board[i][move-1]!=0:
            bascket.append(board[i][move-1])
        board[i][move-1] = 0
        
        if 2<=len(bascket) and bascket[-1]==bascket[-2]:
            bascket.pop()
            bascket.pop()
            answer+=2
        
    return answer