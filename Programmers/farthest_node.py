# https://programmers.co.kr/learn/courses/30/lessons/49189
# 처음 다익스트라 사용했는데 뭐때문인지 채점에서 틀림; 그래서 일반 BFS 를 사용함
# (아마 graph initialize 하는 곳에서 틀린게 아닌가 싶다)
# cost 계산하는거 조금 주의 할 필요있음

from collections import deque

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for e in edge:
        a = e[0]
        b = e[1]
        graph[a].append(b)
        graph[b].append(a)
        
    queue = deque([1])
    distance[1] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            cost = distance[v] + 1
            if cost < distance[i]:
                distance[i] = cost
                queue.append(i)
            
    for idx, i in enumerate(distance):
        if i == INF:
            distance.pop(idx)
            
    for i in distance:
        if i == max(distance):
            answer += 1
    # print(distance[1:])
    
    return answer
[출처] 가장 먼 노드|작성자 hsssy01
