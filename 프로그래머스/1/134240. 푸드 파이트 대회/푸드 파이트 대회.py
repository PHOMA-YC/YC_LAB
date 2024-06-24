def solution(food):
    food_copy = list(map(lambda x: x//2, food)) #--> i는 음식, idx는 먹는음식의 갯수
    answer = ''
    result = ''
    # 반 짤라서 앞배열 생성 후 뒤집어서 붙여
    for idx, i in enumerate(food):
        if i <= 1:
            continue
        else:
            answer += str(idx) * food_copy[idx]
            
    result += answer
    result += '0'
    result += answer[::-1]

    return result
            