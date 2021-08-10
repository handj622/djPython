# DFS 매서드 정의
'''
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph =[
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

dfs(graph, 1, visited)
'''
# BFS 매서드 정의
'''
from collections import deque

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

'''
DFS ( Depth-First Search ) : 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.
=> 그래프의 기본 구조
그래프 : 노드(Node)와 간선(Edge)으로 표현되며 이때 노드를 정점(Vertex)이라고도 말한다.
그래프탐색 : 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다. 또한 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다(Adjacent)'라고 표현한다.
ex_Node_and_Edge) : 노드를 도시 간선을 도로라고 생각하면 된다.
<프로그래밍에서의 그래프>
인접 행렬 ( Adjacency Matrix ) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
인접 리스트 ( Adjacency List ) : 리스트로 그래프의 연결 관계를 표현하는 방식
DFS는 깊이 우선 탐색 알고리즘이라고 했다
이 알고리즘은 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘이다.
DFS는 스택 자료구조를 이용한다.

BFS ( Breadth First Search ) : 너비 우선 탐색이라는 의미를 가진다. 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다.
DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작한다고 했는데 BFS는 그 반대이다.
BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다.
인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행하게 된다.


                DFS             BFS
동작 원리         스택              큐
구현 방법         재귀 함수 이용      큐 자료구조 이용
'''

'''
어제 배웠던 내용은 오늘의 내용을 더불어 설명하기 위함이었다.
스택을 사용하는 DFS알고리즘과 큐를 이용하는 BFS알고리즘을 위해 말이다.
근데 원리는 다 이해가 간다. 자료구조에서 배웠던 트리의 개념과 비슷했기 때문이다.
하지만 코드가 잘 이해가 되지 않는다.
내일 DFS와 BFS의 예제에 쓰인 코드를 잘 이해해야 앞으로 있을 문제에 대해 생산적인 고민들을 많이 할 수 있을것 같다.
내일의 목표는 DFS와 BFS의 예제에 쓰인 코드를 이해하고 한 문제를 풀어보는 것이다.
'''