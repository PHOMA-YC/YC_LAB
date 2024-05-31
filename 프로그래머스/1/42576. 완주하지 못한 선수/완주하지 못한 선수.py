# def solution(participant, completion):
    
#     for i in range(len(participant)) :   
#       isData=0 # 없다   
#       for j in range(len(completion)) :
#         if participant[i]==completion[j] :
#            isData=1 # 있다 
#            completion.remove(participant[i])
#            break
        
#       if isData==0 :
#         return participant[i]     
    
    
    

    
def solution(participant, completion):

    p_list = sorted(participant)
    c_list = sorted(completion)
    

    for p, c in zip(p_list, c_list):
        if p != c:
            return p
        
    return p_list[-1]
