def solution(food):
    food_list = [1]
    result = ''
    
    for i in food[1:]:
        if i % 2 == 0 :
            food_list.append(i)
        else:
            food_list.append(i-1)
            
    for idx, i in enumerate(food_list[1:]):
        if i == 0 :
            continue
        else :        
            result += str(idx+1) * (i // 2)
        
    reverse_result = result[::-1]
    
    return result + '0' + reverse_result