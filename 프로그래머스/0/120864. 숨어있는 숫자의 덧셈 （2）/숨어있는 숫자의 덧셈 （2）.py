def solution(my_string):
    answer= ""
    for i in my_string:
        if i.isdigit():
            answer += i
            
        else :
            answer += ' '
            
    x = answer.strip().split()
    result = 0
    for i in x :
        result += int(i)
        
    return result
        