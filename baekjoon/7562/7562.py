'''
나이트의 이동 python 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EC%9D%B4%ED%8A%B8%EC%9D%98-%EC%9D%B4%EB%8F%99-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs(a,b,c,d):
	dx=[-1,1,2,2,1,-1,-2,-2]
	dy=[2,2,1,-1,-2,-2,-1,1]
	queue=deque()
	queue.append((a,b))
	while queue:
		x,y=queue.popleft()
		if x==c and y==d:
			return graph[x][y]-1
		for i in range(8):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
				graph[nx][ny]=graph[x][y]+1
				queue.append((nx,ny))

t=int(input())
for _ in range(t):
	l=int(input())
	cx,cy=map(int,input().split())
	ox,oy=map(int,input().split())
	graph=[[0]*l for i in range(l)]
	graph[cx][cy]=1
	print(bfs(cx,cy,ox,oy))
