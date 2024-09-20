def solution(numbers, hand):
    my_dict = {1:(0,0),2:(0,1),3:(0,2),
               4:(1,0),5:(1,1),6:(1,2),
               7:(2,0),8:(2,1),9:(2,2),
               '*':(3,0), 0:(3,1),'#':(3,2)}
    result = ''
    now_L = '*'
    now_R = '#'
    for i in numbers :
        if i in [1,4,7]:
            result += 'L'
            now_L = i
            continue
        if i in [3,6,9]:
            result += 'R'
            now_R = i
            continue
        else :
            x1,y2 = my_dict[i]
            r1,r2 = my_dict[now_R]
            l1,l2 = my_dict[now_L]
            R = abs((x1-r1))+ abs((y2-r2))
            L = abs((x1-l1))+ abs((y2-l2))
            if R == L :
                if hand == 'right' :
                    result += 'R'
                    now_R = i
                else :
                    result += 'L'
                    now_L = i
            else :
                if R < L :
                    result +='R'
                    now_R = i
                elif R > L :
                    result += 'L'
                    now_L = i
                    
    return result
                
            