# BFS : 너비 우선 탐색 (Breadth-First-Search)
# BFS 연습문제

from collections import deque

def bfs(graph, start, visited):
    # Queue 자료구조 사용하기 위해서 deque 라이브러리를 사용
    queue = deque([start])
    visited[start] = True

    # queue가 비어있을 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

bfs(graph, 1, visited)