def solution(num_list, n):
    new_list = []
    for i in range(0, len(num_list), n):
        new_list.append(num_list[i : i + n])
        
    return new_list