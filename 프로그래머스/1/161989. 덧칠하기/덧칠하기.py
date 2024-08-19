def solution(n, m, section):
    section = sorted(section)
    result = 0
    wall = [k for k in range(1, n+1)]
    if m == 1 :
        return len(section)
    else :
        while section:
            start = section[0]
            end = start + m
            section = [x for x in section if x >= end]
            result += 1
        
        return result