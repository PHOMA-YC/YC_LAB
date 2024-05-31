def solution(s):
    if s.isdigit() == False :
        return False
    elif len(s) == 4 :
        return True
    elif len(s) == 6 :
        return True
    else :
        return False
    
    
    