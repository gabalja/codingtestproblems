'''
Two Dots python 풀이
https://doctcoder.tistory.com/entry/Two-Dots-%ED%92%80%EC%9D%B4
'''
def dfs(a,b,c,d,e):
	dx=(1,0,-1,0)
	dy=(0,1,0,-1)
	if visit[a][b]:
		print("Yes")
		exit()
	visit[a][b]=True
	for i in range(4):
		nx=a+dx[i]
		ny=b+dy[i]
		if not (0<=nx<n and 0<=ny<m) or graph[nx][ny]!=c:
			continue
		if (nx,ny)==(d,e):
			continue
		dfs(nx,ny,c,a,b)

n,m=map(int,input().split())
graph=[list(input()) for _ in range(n)]
visit=[[False]*m for i in range(n)]
for i in range(n):
	for j in range(m):
		if not visit[i][j]:
			dfs(i,j,graph[i][j],-1,-1)
print("No")
