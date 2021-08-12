def dfs(graph, v, visited):
    visited[v] = True
    #print(v, end=' ')

    for i in graph[v]:
        #print('i의 값',i)
        #print(graph[i])
        #print(visited[i])
        #print('\n')
        print(i)
        #print(graph[i])
        if not visited[i]:
            print("WOW")
            print('\n')
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)


'''

오늘 뭔가 많이 알아낸것 같지만 정리는 잘 되지 않는다.
그 이유는 아직 for i in graph[v]가 지금 어떻게 작동되고 있는지 모르는 까닭인것 같다.
처음에 계속 이해가 가지 않았던 부분은 뭐였냐면 graph가 저렇게 되어있는데 어떻게 1,2,7,6,8,3,4,5 라는 결과값이 나오는지에 대해서 문제의식을 갖고 있었던것 같다.
다시말해 이 코드가 작동하는데에는 함수인 dfs(graph,v,visited) 이 부분이었다는것을 인지하지 못하고 있었다.  graph는 그냥 정보라고 생각하면 되는거였는데
graph가 작동하는 코드인것 마냥 이상하게 꼬여서 접근하고 있었다. 그래서 dfs에 초점을 두고 이것저것 이해를 위해 추가해보고 빼보고 여기서 지금 어떤 숫자와 결과값이
나오는지 중간중간 테스트도 해보고 고민하다가 시간이 다갔다.
dfs와bfs 를 이번기회에 제대로 이해하고 가고 싶다. 도움이 많이 될것같다.


'''