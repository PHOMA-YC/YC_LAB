def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    def dfs(computers, visited, start):
        stack = [start]
        
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
                
            for i in range(len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)
    
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    
    return answer