'''
BFS 스페셜 저지 python 풀이
https://doctcoder.tistory.com/entry/BFS-%EC%8A%A4%ED%8E%98%EC%85%9C-%EC%A0%80%EC%A7%80-%ED%92%80%EC%9D%B4
'''
import sys
from collections import deque
input=sys.stdin.readline
 
def bfs(s):
    visited=[False]*(n+1)
    q=deque()
    q.append(s)
    ret=[1]
    visited[s]=True 
    while q:
        start = q.popleft()
        for node in graph[start]:
            if not visited[node]:
                q.append(node)
                visited[node]=True
                ret.append(node)
    return ret
 
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result=list(map(int, input().split()))
order=[0]*(n+1)
for i in range(len(result)):
    order[result[i]]=i
for i in range(1, len(graph)):
    graph[i].sort(key=lambda x:order[x])
ret=bfs(1)
if ret==result:
    print(1)
else:
    print(0)
