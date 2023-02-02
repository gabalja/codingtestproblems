'''
DFS와 BFS python 풀이
https://doctcoder.tistory.com/entry/DFS%EC%99%80-BFS-%ED%92%80%EC%9D%B4
'''
from collections import deque

def dfs(v):
	dvisit[v]=True
	print(v,end=' ')
	for i in range(1,n+1):
		if not dvisit[i] and mat[v][i]:
			dfs(i)

def bfs(v):
	q=deque([v])
	bvisit[v]=True
	while q:
		v=q.popleft()
		print(v,end=' ')
		for i in range(1,n+1):
			if not bvisit[i] and mat[v][i]:
				q.append(i)
				bvisit[i]=True

n,m,v=map(int,input().split())
mat=[[False]*(n+1) for i in range(n+1)]
for i in range(m):
	a,b=map(int,input().split())
	mat[a][b]=True
	mat[b][a]=True
dvisit=[False]*(n+1)
bvisit=[False]*(n+1)
dfs(v)
print()
bfs(v)
