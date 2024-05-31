def solution(answers):
    no_1 = [1,2,3,4,5]
    no_2 = [2,1,2,3,2,4,2,5]
    no_3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    while len(no_1) < len(answers) :
        no_1.extend(no_1)
        
    no_1 = no_1[:len(answers)]
            
    while len(no_2) < len(answers) :
        no_2.extend(no_2)
        
    no_2 = no_2[:len(answers)]
            
    while len(no_3) < len(answers) :
        no_3.extend(no_3)
        
    no_3 = no_3[:len(answers)]
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in range(len(answers)) :
        if answers[i] == no_1[i] :
            count_1 += 1
        if answers[i] == no_2[i] :
            count_2 += 1
        if answers[i] == no_3[i] :
            count_3 += 1
            
    result = []
    
    result.append(count_1)
    result.append(count_2)
    result.append(count_3)
            
        
    result_list = []
    
    if max(result) == result[0] :
        result_list.append(1)
    if max(result) == result[1] :
        result_list.append(2)
    if max(result) == result[2] :
        result_list.append(3)
    
    return result_list
    
   

