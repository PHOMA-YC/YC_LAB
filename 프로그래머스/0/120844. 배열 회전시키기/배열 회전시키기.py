def solution(numbers, direction):
    if direction == "right":
        return numbers[-1:] + numbers[:-1]
    else :
        return numbers[1:] + numbers[:1]

    
# 리스트를 슬라이싱하면 리스트가 나온다.
# 리스트와 리스트 끼리 연산이 가능하다 ( +/- ).
# 슬라이싱할 때, 끝지점이 -1 이면 끝에서 한칸 바로 앞까지 슬라이싱한다.