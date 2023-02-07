'''
토마토 python 풀이
https://doctcoder.tistory.com/entry/%ED%86%A0%EB%A7%88%ED%86%A0-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs():
	dx=[-1,1,0,0]
	dy=[0,0,-1,1]
	queue=deque([])
	for i in range(n):
		for j in range(m):
			if graph[i][j]==1:
				queue.append([i,j])
	while queue:
		x,y=queue.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
				graph[nx][ny]=graph[x][y]+1
				queue.append([nx,ny])

m,n=map(int,input().split())
graph=[list(map(int,input().split())) for i in range(n)]
bfs()
res=0
for i in graph:
	for j in i:
		if j==0:
			print(-1)
			exit(0)
	res=max(res,max(i))
print(res-1)
