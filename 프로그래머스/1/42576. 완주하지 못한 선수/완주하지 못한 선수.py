def solution(participant, completion):
    
    for i in range(len(participant)) :   
      isData=0 # 없다   
      for j in range(len(completion)) :
        if participant[i]==completion[j] :
           isData=1 # 있다 
           completion.remove(participant[i])
           break
        
      if isData==0 :
        return participant[i]     