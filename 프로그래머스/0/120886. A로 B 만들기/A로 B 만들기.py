def solution(before, after):
    result = []
    before = list(before)
    after = list(after)
    for i in before :
        if i in after :
            result.append(1)
            after.remove(i)
        else :
            result.append(0)
        
    if result.count(1) == len(before) :
        return 1
    else :
        return 0
        
        
            