def solution(t, p):
    len_P = len(p)
    len_T = len(t)
    answer = 0
    for i in range(len_T - len_P + 1):
        if int(t[i:len_P+i]) <= int(p):
            answer +=1
    
    return answer