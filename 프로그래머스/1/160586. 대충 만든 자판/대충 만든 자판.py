def solution(keymap, targets):
    answer = {}
    for key in keymap:
        for i, chr in enumerate(key):
            if chr not in answer or answer[chr]>i:
                answer[chr]=i+1
    result_list = []
    for target in targets:
        total_sum = 0
        isPossible = True
        
        for chr in target:
            if chr in answer:
                total_sum += answer[chr]
            else:
                isPossible = False
                break
        if isPossible:
            result_list.append(total_sum)
        else:
            result_list.append(-1)
    return result_list