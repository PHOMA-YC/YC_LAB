def solution(my_string):
    num_list = []
    count = 0
    for i in range(10):
        num_list.append(str(i))
        
        
    for i in my_string :
        if i in num_list :
            count += int(i)
            
    return count
            
        