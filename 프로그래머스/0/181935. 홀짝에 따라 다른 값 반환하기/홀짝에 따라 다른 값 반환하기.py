def solution(n):
    result = 0
    if n % 2 != 0 :
        result += sum([i for i in range(1,n+1,2)])
    else :
        result += sum([(j**2) for j in range(0,n+1,2)])
    
    return result
        
    
        
                
            