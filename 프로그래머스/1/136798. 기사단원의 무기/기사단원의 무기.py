import math
def solution(number, limit, power):
    if number == 1 :
            return 1


    entry = [i for i in range(2,number+1)]
    result = [1]
    for i in entry :
        cnt = 0
        for j in range(1, int(math.sqrt(i+1))+1) :

            if i % j == 0 :
                cnt += 1

        if math.sqrt(i) == int(math.sqrt(i)) : # 제곱근
            result.append(((cnt - 1) * 2) + 1)
        else :
            result.append(cnt*2)
    
    return sum([x if x <= limit else power for x in result])