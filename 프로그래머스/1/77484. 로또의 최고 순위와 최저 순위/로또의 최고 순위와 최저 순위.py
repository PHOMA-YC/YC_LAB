def solution(lottos, win_nums):
    winner = {6 : 1 , 5 : 2 , 4 : 3, 3 : 4, 2 : 5}
    zeros = lottos.count(0)
    if zeros :
        for _ in range(zeros) :
            lottos.remove(0)
    print(lottos)
    
    best = zeros
    worst = 0
    
    for i in lottos :
        if i in win_nums :
            best += 1
            worst += 1
    
    if best in winner:
        result = [winner[best]]
    else :
        result = [6]
    
    if worst in winner:
        result.append(winner[worst])
    else :
        result.append(6)
        
    return result