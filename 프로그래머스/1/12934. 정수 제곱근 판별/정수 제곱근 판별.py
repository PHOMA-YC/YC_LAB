import math
def solution(n):
    root = math.sqrt(n)
    if root != int(root):
        return -1
    else :
        return (root+1) ** 2