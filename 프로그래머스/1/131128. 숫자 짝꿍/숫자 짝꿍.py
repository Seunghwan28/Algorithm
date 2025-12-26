from collections import Counter
def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)
    answer = []
    for i in range(9,-1,-1):
        char = str(i)
        count = min(count_X[char], count_Y[char])
        answer.append(char*count)
    ans = "".join(answer)
    if not ans:
        return "-1"
    if ans[0] == "0":
        return "0"
    return ans
