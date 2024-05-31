def solution(my_string):
    z = ['a', 'e', 'i', 'o', 'u']
    for i in my_string :
        if i in z :
            my_string = my_string.replace(i, '')
        
    return my_string