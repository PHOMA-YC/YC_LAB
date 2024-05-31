def solution(n):
    a_list = []
    
    i = 0
    while i < n :
        a_list.append('수')
        i += 1
        if i < n :
            a_list.append('박')
            i += 1
        
    return ''.join(a_list)
    
    