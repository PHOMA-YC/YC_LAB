def solution(hp):
    result = 0
    hp1 = hp % 5
    result += hp // 5
    hp2 = hp1 % 3
    result += hp1 //3
    hp3 = hp2 % 1
    result += hp2 //1
    
    return result
    
     
                        