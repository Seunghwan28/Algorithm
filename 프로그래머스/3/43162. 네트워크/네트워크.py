def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(node):
        visited[node] = True
        
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
    
    for j in range(n):
        if not visited[j]:
            dfs(j)
            answer += 1
    
    return answer