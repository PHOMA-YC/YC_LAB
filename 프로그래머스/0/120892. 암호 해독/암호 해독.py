def solution(cipher, code):
    real_code = []
    i = 1
    while code * i <= len(cipher):
        real_code.append(cipher[(code * i) -1])
        i += 1
        
    
    return ''.join(real_code)
        