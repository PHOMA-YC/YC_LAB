def solution(A, B):
    if A == B :
        return 0
    cnt = 0
    for i in range(len(A)) : 
        if B == A[-i:] + A[:-i] :
            return cnt
        cnt += 1
        
    return -1