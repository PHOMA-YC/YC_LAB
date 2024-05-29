def solution(age):
    answer = ''
    age_l = ['a','b','c','d','e','f','g','h','i','j']
    age = str(age)
    for i in age:
        answer += age_l[int(i)]
        
    return answer