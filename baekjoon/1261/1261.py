'''
알고스팟 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%EA%B3%A0%EC%8A%A4%ED%8C%9F-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs():
	dx=[-1,1,0,0]
	dy=[0,0,-1,1]
	q=deque()
	q.append((0,0))
	visited[0][0]=0
	while q:
		x,y=q.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<m:
				if visited[nx][ny]==-1:
					if inp[nx][ny]==0:
						visited[nx][ny]=visited[x][y]
						q.appendleft((nx,ny))
					else:
						visited[nx][ny]=visited[x][y]+1
						q.append((nx,ny))

m,n=map(int,input().split())
inp=[list(map(int,input())) for i in range(n)]
visited=[[-1]*m for i in range(n)]
bfs()
print(visited[n-1][m-1])
