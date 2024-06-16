def solution(s):
    my_dict = {0:'zero', 1:'one', 2:'two',3:'three', 4:'four', 5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    for k,v in my_dict.items():
        if v in s :
            s = s.replace(v,str(k))
            
    return int(s)
            
                