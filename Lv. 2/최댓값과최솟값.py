def solution(s):
    s_list = list(map(int, s.split()))
    s_min = min(s_list)
    s_max = max(s_list)
    
    answer = str(s_min) + ' ' + str(s_max)
    
    return answer
