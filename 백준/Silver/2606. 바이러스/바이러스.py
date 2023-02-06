t = int(input())
s = int(input())
graph = [[]*t for _ in range(t+1)]
for _ in range(s):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


v = [False] * (t+1)
cnt = 0

def dfs(start) :
    stack = [start]
    v[start] = True

    while stack :  #스택이 비워있지 않을 때
        cur = stack.pop()
        global cnt
        cnt+=1
        for adj in graph[cur] :
            if not v[adj] :
                v[adj] = True
                stack.append(adj)
dfs(1)                
print(cnt-1)
