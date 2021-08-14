from collections import deque # ??

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

'''
어후야 길고긴 대장정이 끝난 느낌이다. 
DFS 와 BFS의 기본 개념을 제대로 집고 넘어간것 같아 매우 다행이다.
이제 내일부터 문제풀이에 들어가야겠다. 
구다형 땡큐
'''