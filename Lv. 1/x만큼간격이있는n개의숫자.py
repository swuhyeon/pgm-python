def solution(x, n):
    answer = []
    number = x
    
    for i in range(n):
        answer.append(number)
        number += x
        
    return answer
