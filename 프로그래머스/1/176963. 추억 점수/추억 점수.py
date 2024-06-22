def solution(name, yearning, photo):
    my_dict = {}
    answer = []
    for idx, i in enumerate(name) :
        my_dict[i] = yearning[idx]
        
    for x in photo :
        count = 0
        for y in x :
            if y in my_dict :
                count += my_dict[y]
        answer.append(count)
        
    return(answer)