'''
DFS 스페셜 저지 python 풀이
https://doctcoder.tistory.com/entry/DFS-%EC%8A%A4%ED%8E%98%EC%85%9C-%EC%A0%80%EC%A7%80-%ED%92%80%EC%9D%B4
'''
import sys
N = int(sys.stdin.readline())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
ans= list(map(int,sys.stdin.readline().split()))
level=[False]*(N+1)
tsize = [0]*(N+1)
visited = [False]*(N+1)

def dfs(x,lv):
    if visited[x]:
        return 0
    visited[x]=True
    size=1
    level[x]=lv
    for i in range(len(graph[x])):
        next =graph[x][i]
        size+=dfs(next,lv+1)
    tsize[x]=size
    return size


if ans[0]!=1:
    print("0")
    sys.exit(0)
else:
    dfs(1,0)
    for i in range(1,N):
        x=ans[i]
        if tsize[x] == 1 or i + tsize[x] >=N:
            continue
        next = ans[i+tsize[x]]
        if level[next]>level[x]:
            print(0)
            sys.exit(0)
    print(1)
