def solution(array):
    u = set(array)
    my_dict = {}
    for i in u :
        my_dict[i] = array.count(i)
    result = [k for k, v in my_dict.items() if max(my_dict.values()) == v]
    
    if len(result) >= 2 :
        return -1
    else :
        return result[0]