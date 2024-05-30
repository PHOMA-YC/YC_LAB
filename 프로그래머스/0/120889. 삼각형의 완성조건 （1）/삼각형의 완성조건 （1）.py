def solution(sides):
    a = max(sides)
    sides.remove(max(sides))
    if a < sum(sides) :
        return 1
    else :
        return 2