'''
다리 만들기 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A4%EB%A6%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
from collections import deque

def island(a,b):
	q=deque()
	q.append([a,b])
	while q:
		x,y=q.popleft()
		for (h,w) in [[1,0],[0,1],[-1,0],[0,-1]]:
			dx,dy=x+h,y+w
			if 0<=dx<n and 0<=dy<n and not visited[dx][dy] and inp[dx][dy]:
				visited[dx][dy]=1
				inp[dx][dy]=num
				q.append([dx,dy])

def bfs(v):
	q=deque()
	dis=[[-1]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			if inp[i][j]==v:
				dis[i][j]=0
				q.append([i,j])
	while q:
		x,y=q.popleft()
		for (w,h) in [[1,0],[0,1],[-1,0],[0,-1]]:
			dx,dy=x+w,y+h
			if 0<=dx<n and 0<=dy<n:
				if inp[dx][dy] and inp[dx][dy]!=v:
					return dis[x][y]
				elif (not inp[dx][dy]) and dis[dx][dy]==-1:
					dis[dx][dy]=dis[x][y]+1
					q.append([dx,dy])
	return int(1e9)

n=int(input())
inp=[list(map(int,input().split())) for i in range(n)]
visited=[[0]*n for i in range(n)]
num=1
res=int(1e9)
for i in range(n):
	for j in range(n):
		if inp[i][j] and not visited[i][j]:
			visited[i][j]=1
			inp[i][j]=num
			island(i,j)
			num+=1
for i in range(1,num):
	res=min(res,bfs(i))
print(res)
