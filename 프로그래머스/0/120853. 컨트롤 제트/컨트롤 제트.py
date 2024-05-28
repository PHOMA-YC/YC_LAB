def solution(s):
    s_list = s.split(' ')
    new_list = []
    for i in range(len(s_list)):
        if s_list[i] != 'Z' :
            new_list.append(int(s_list[i]))
        elif s_list[i] == 'Z' :
            new_list.remove(new_list[-1])
            
    return sum(new_list)
            
        