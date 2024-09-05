def solution(ineq, eq, n, m):
    x = ineq + eq
    if x == '>=' :
        if n >= m :
            return 1
        else :
            return 0
    elif x == '<=' :
        if n <= m :
            return 1
        else :
            return 0
    elif x == '>!' :
        if n > m :
            return 1
        else :
            return 0
    elif x == '<!':
        if n < m :
            return 1 
        else :
            return 0
