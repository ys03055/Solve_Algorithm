from collections import deque
import sys
input = sys.stdin.readline

N,M,R = map(int, input().split())

graph = [[] for i in range(N+1)]
for _ in range(M) :
    U,V = map(int,input().split())
    graph[U].append(V)
    graph[V].append(U)
    
visited = [0] * (N+1)
visited[R] = 1

queue = deque([R])
cnt = 1

while queue :
    node = queue.popleft()
    graph[node].sort() 
    for next_node in graph[node] :
        if not visited[next_node] :
            cnt +=1
            queue.append(next_node)
            visited[next_node] = cnt

for i in visited[1:] :
    print(i)
