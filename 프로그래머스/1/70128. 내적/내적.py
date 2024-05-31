def solution(a, b):
    result = []
    for x,y in zip(a,b) :
        result.append(x * y)
        
    return sum(result)