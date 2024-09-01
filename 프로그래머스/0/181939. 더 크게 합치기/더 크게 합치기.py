def solution(a, b):
    if str(a)+str(b) == str(b)+str(a) :
        return int(str(a)+str(b))
    return max(int(str(a)+str(b)) ,int(str(b)+str(a)))