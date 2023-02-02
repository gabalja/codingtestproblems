'''
단지번호붙이기 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs(g,a,b):
	q=deque()
	q.append([a,b])
	g[a][b]=0
	cnt=1
	while q:
		x,y=q.popleft()
		g[x][y]=0
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if nx<0 or nx>=len(g) or ny<0 or ny>=len(g):
				continue
			if g[nx][ny]==1:
				g[nx][ny]=0
				q.append([nx,ny])
				cnt+=1
	return cnt

n=int(input())
graph=[]
res=[]
for _ in range(n):
	graph.append(list(map(int,input())))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for i in range(n):
	for j in range(n):
		if graph[i][j]==1:
			cnt=bfs(graph,i,j)
			res.append(cnt)
res.sort()
print(len(res))
for i in res:
	print(i)
