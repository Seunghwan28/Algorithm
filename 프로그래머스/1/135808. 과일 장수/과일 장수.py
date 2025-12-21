import heapq

def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    n = len(score) // m
    for i in range(n):
        min_heap = []
        for j in range(m):
            heapq.heappush(min_heap, score[i*m+j])
        answer += min_heap[0]*m
    
    return answer