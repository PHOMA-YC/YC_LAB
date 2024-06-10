def solution(citations):
    citations = sorted(citations)
    n = 0
    while True :
        if n <= len([i for i in citations if i >= n]) :
            n += 1
        else :
            break
    return n - 1