# DFS : 깊이 우선 탐색
# DFS 연습문제

def dfs(graph, vertex, visited):
    # 현재의 노드를 방문 처리함
    visited[vertex] = True
    print(vertex, end=" ")
    for i in graph[vertex]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],    # 1번 노드와 인접한 노드
    [1,7],      # 2번 노드와 인접한 노드
    [1,4,5],    # 3번 노드와 인접한 노드
    [3,5],      # 4번 노드와 인접한 노드
    [3,4],      # 5번 노드와 인접한 노드
    [7],        # 6번 노드와 인접한 노드
    [2,6,8],    # 7번 노드와 인접한 노드
    [1,7],      # 8번 노드와 인접한 노드
]

visited = [False] * 9

dfs(graph, 1, visited)