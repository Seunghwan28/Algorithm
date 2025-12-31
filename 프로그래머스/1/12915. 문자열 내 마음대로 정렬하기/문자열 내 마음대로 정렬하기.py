def solution(strings, n):
    answer = []

    answ = []
    strings.sort()
    for i in range(len(strings)):
        row = []
        for j in range(len(strings[i])):
            row.append(strings[i][j])
        answer.append(row)
    
    result = sorted(answer, key=lambda x: x[n])
    for i in range(len(result)):
        ans = ''
        for j in range(len(result[i])):
            ans += result[i][j]
        answ.append(ans)
    return answ