def solution(board, moves):
    checkpoint = [0 for _ in range(len(board))]
    Checkpoint = [checkpoint[:] for _ in range(len(board))]
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    basket = []
    removed = 0
    
    for move in moves :
        col = move -1 
        
        for row in range(len(board)):
            if board[row][col] != 0 :
                doll = board[row][col]
                board[row][col] = 0
                
                if basket and basket[-1] == doll :
                    basket.pop()
                    removed += 2
                
                else :
                    basket.append(doll)
                    
                break
                
    return removed
                