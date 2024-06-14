def solution(t, p):
    answer = []
    result = 0
    for i in range(len(t)-len(p)+1) :
        answer.append(t[i:len(p)+i])
    
    for j in answer :
        if int(j) <= int(p) :
            result += 1
            
    return result
        